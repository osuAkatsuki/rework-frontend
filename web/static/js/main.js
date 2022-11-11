
const modsObj = {
    "NF": 1,
    "EZ": 2,
    "TD": 4, // Previously used for NV
    "HD": 8,
    "SD": 32,
    "DT": 64,
    "NC": 512,
    "RX": 128,
    "HT": 256,
    "HR": 16,
    "FL": 1024,
    "AU": 2048,
    "AP": 8192,
    "PF": 16384,
    "SO": 4096,
    "K4": 32768,
    "K5": 65536,
    "K6": 131072,
    "K7": 262144,
    "K8": 524288,
    "FI": 1048576,
    "RN": 2097152,
    "LM": 4194304,
    "K9": 16777216,
    "K1": 33554432,
    "K3": 67108864,
    "K2": 134217728,
    "S2": 536870912,
    "MR": 1073741824
};

function removeFromArray(array, value) {
    const index = array.indexOf(value);

    if (index > -1) {
        array.splice(index, 1);
    }
}

function invokeDropdownMenu(dropdownInvoker) {
    dropdownType = $(dropdownInvoker).data("menu");

    dropdown = $(`[data-dropdown-menu="${dropdownType}"]`);
    dropdownIcon = $(`[data-dropdown-icon="${dropdownType}"]`);

    if (dropdown.hasClass("hidden")) {
        dropdown.slideDown(300, () => {
            dropdown.removeClass("hidden");
            dropdownIcon.removeClass("fa-chevron-down");
            dropdownIcon.addClass("fa-chevron-up");
        })
    } else {
        dropdown.slideUp(300, () => {
            dropdown.addClass("hidden");
            dropdownIcon.removeClass("fa-chevron-up");
            dropdownIcon.addClass("fa-chevron-down");
        })
    }
}

function getScoreMods(n) {

    const _modsString = Object.keys(modsObj);
    const mods = JSON.parse(JSON.stringify(modsObj));
    const playmods = [];

    if (!n) {
        return "NM"
    }

    for (let mod = 0; mod < _modsString.length; mod++) {
        if (mods[_modsString[mod]] != 0 && (n & mods[_modsString[mod]])) {
            playmods.push(_modsString[mod]);
        }
    }

    // has nc => remove dt
    if (n & mods.NC) {
        removeFromArray(playmods, "DT")
    } else if (n & mods.DT) {
        removeFromArray(playmods, "NC")
    }

    // has pf => remove sd
    if (n & mods.PF) {
        removeFromArray(playmods, "SD")
    } else if (n & mods.SD) {
        removeFromArray(playmods, "PF")
    }

    return playmods.join("");
}

function renderDelta(old, _new) {
    delta = (_new - old).toFixed(2)

    if (delta < 0) {
        return `
        (+${numberCommas(Math.abs(delta))}
            <div class="inline-block before:content-['▲'] text-green-600"></div>
        )`
    } else if (delta > 0) {
        return `
        (-${numberCommas(Math.abs(delta))}
            <div class="inline-block before:content-['▼'] text-red-500"></div>
        )`
    } else {
        return `
        (${numberCommas(Math.abs(delta))}
            <div class="inline-block before:content-['▬'] text-gray-500"></div>
        )`
    }
}

function country(country) {
    chars = []
    country = country.toUpperCase()

    for (let i = 0; i < country.length; i++) {
      chars.push(
        (country.codePointAt(i) + 127397).toString(16)
      )
    }

    return chars.join("-")
}

function numberCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function debounceInput(func, delay = 1000) {
    let timer;
    return function(...args) {
       const context = this;
       clearTimeout(timer);
       timer = setTimeout(() => {
           func.apply(context, args);
       }, delay)
     }
}
