var usersTable = $("#leaderboard-users-table")
var showingFrom = $("#number-showing-from")
var showingTo = $("#number-showing-to")
var userEntries = $("#number-enteties")
var searchBar = $("#search-user-box")
var searchResults = $("#search-user-results")

const PAGE_LIMIT = 50
const SPINNING_CIRCLE = `
<tr
    id="spinning-empty-circle"
    class="border-b border-gray-200 dark:border-gray-700"
    >
    <td colspan="9" class="py-4 px-6 bg-gray-50 dark:bg-gray-800">
        <div class="flex justify-center">
        <div role="status">
            <svg
            class="inline w-14 h-14 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
            viewBox="0 0 100 101"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            >
            <path
                d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                fill="currentColor"
            />
            <path
                d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                fill="currentFill"
            />
            </svg>
            <span class="sr-only">Loading...</span>
        </div>
        </div>
    </td>
</tr>
`
const SPINNING_SEARCH_CIRCLE = `
<div
    class="py-2 w-60 bg-white rounded-md shadow-xl dark:bg-gray-700 dark:divide-gray-600 text-sm z-10 static"
    id="spinning-search-response"
>
    <div
    class="block px-4 py-2 text-gray-900 hover:bg-gray-500 hover:rounded-md hover:bg-opacity-25 dark:text-white"
    >
        <div class="flex items-center space-x-4">
            <div class="flex justify-center items-center">
                <div role="status">
                    <svg
                    class="inline w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                    viewBox="0 0 100 101"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    >
                    <path
                        d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                        fill="currentColor"
                    />
                    <path
                        d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                        fill="currentFill"
                    />
                    </svg>
                    <span class="sr-only">Loading...</span>
                </div>
            </div>
        </div>
    </div>
</div>`


$(document).ready(function () {
    loadLeaderboard()
})

function loadNextPage(btn) {
    leaderboardConfig.page += 1

    var searchParams = new URLSearchParams(window.location.search)
    searchParams.set("page", leaderboardConfig.page);
    var newRelativePathQuery = window.location.pathname + '?' + searchParams.toString();
    window.history.pushState(null, '', newRelativePathQuery);

    usersTable.empty();
    usersTable.append(SPINNING_CIRCLE)
    loadLeaderboard()
}

function loadPreviousPage(btn) {
    leaderboardConfig.page -= 1

    var searchParams = new URLSearchParams(window.location.search)
    searchParams.set("page", leaderboardConfig.page);
    var newRelativePathQuery = window.location.pathname + '?' + searchParams.toString();
    window.history.pushState(null, '', newRelativePathQuery);

    usersTable.empty();
    usersTable.append(SPINNING_CIRCLE)
    loadLeaderboard()
}


function loadLeaderboard() {
    fetch(`/api/v1/leaderboards/${leaderboardConfig.rework_id}?` + new URLSearchParams({
        page: leaderboardConfig.page,
        limit: PAGE_LIMIT,
    }))
    .then(response => response.json())
    .then(data => {
        if (data.data.users.length === 0) {
            scoreTable.append(`
            <tr class="border-b border-gray-200 dark:border-gray-700">
                <td colspan="9" class="w-full h-full py-4 px-6 bg-gray-50 dark:bg-gray-800">
                    <div class="flex justify-center">
                        <div class="inline dark:text-white text-2xl">
                            No users found :(
                        </div>
                    </div>
                </td>
            </tr>
            `)
            $("#spinning-empty-circle").remove()
            return
        }

        userEntries.text(data.data.total_count)
        showingFrom.text((leaderboardConfig.page - 1) * PAGE_LIMIT + 1)
        showingTo.text((leaderboardConfig.page - 1) * PAGE_LIMIT + data.data.users.length)

        if (leaderboardConfig.page == 1) {
            $("#previous-page-button").attr("disabled", true)
        } else {
            $("#previous-page-button").attr("disabled", false)
        }

        if ((leaderboardConfig.page - 1) * PAGE_LIMIT + data.data.users.length >= data.data.total_count) {
            $("#next-page-button").attr("disabled", true)
        } else {
            $("#next-page-button").attr("disabled", false)
        }

        data.data.users.forEach(user => {
            usersTable.append(`
                    <tr class="border-b border-gray-200 dark:border-gray-700">
                        <td class="py-4 px-6 bg-gray-50 dark:bg-gray-800">
                            #${numberCommas(user['new_rank'])}
                            <br />
                            ${renderDelta(user['old_rank'], user['new_rank'])}
                        </td>
                        <td class="py-4 px-6 dark:bg-gray-700">
                            #${numberCommas(user['old_rank'])}
                        </td>
                        <th
                            class="py-4 px-6 font-medium whitespace-nowrap bg-gray-50 dark:bg-gray-800"
                        >
                            <a
                            href="/rework/${leaderboardConfig.rework_id}/users/${user['user_id']}"
                            >
                            <img
                                src="https://twemoji.maxcdn.com/v/latest/svg/${country(user['country'])}.svg"
                                alt="${user['country']}"
                                class="inline-block h-6 mr-1"
                            />
                            ${user['user_name']}
                            </a>
                        </th>
                        <td class="py-4 px-6 dark:bg-gray-700">
                            ${numberCommas(user['new_pp'])}
                            <br />
                            ${renderDelta(user['new_pp'], user['old_pp'])}
                        </td>
                        <td class="py-4 px-6 bg-gray-50 dark:bg-gray-800">
                            ${numberCommas(user['old_pp'])}
                        </td>
                    </tr>
            `)
        })
        $("#spinning-empty-circle").remove()
    })
}

const onSearchBoxInput = debounceInput(loadUserCardsFromInput, 1000)

searchBar.on("input", () => {
    value = searchBar.val()
    if (value.length == 0 && !searchResults.hasClass("hidden")) {
        searchResults.addClass("hidden")
        searchResults.empty()
        return
    }

    if ($("#spinning-search-response").length == 0) {
        searchResults.empty()
        searchResults.append(SPINNING_SEARCH_CIRCLE)
    }

    if (value.length > 0 && searchResults.hasClass("hidden")) {
        searchResults.removeClass("hidden")
    }

    if (value.length > 0) {
        onSearchBoxInput(value)
    }
})

searchBar.on("focusout", () => {
    setTimeout(() => {
        searchResults.addClass("hidden")
    }, 100)
})

searchBar.on("focusin", () => {
    value = searchBar.val()
    if (value.length > 0 && searchResults.hasClass("hidden")) {
        searchResults.removeClass("hidden")
    }
})

function loadUserCardsFromInput(input) {
    fetch("/api/v1/users?" + new URLSearchParams({
        query: input,
        rework_id: leaderboardConfig.rework_id,
    }))
    .then(response => response.json())
    .then(data => {
        if (data.status == "error") {
            searchResults.empty()
            searchResults.append(`
                <div
                    class="py-2 w-60 bg-white rounded-md shadow-xl dark:bg-gray-700 dark:divide-gray-600 text-sm z-10 static"
                    >
                    <div
                        class="block px-4 py-2 text-gray-900 hover:bg-gray-500 hover:rounded-md hover:bg-opacity-25 dark:text-white"
                    >
                        <div class="flex items-center space-x-4">
                            <div>
                                <p class="font-semibold">No users found :(</p>
                            </div>
                        </div>
                    </div>
                </div>
            `)
            return
        }

        sliced = data.data.slice(0, 5)
        searchResults.empty()
        sliced.forEach((user, index) => {
            searchResults.append(`
            <div
                class="py-2 w-60 bg-white rounded-md shadow-xl dark:bg-gray-700 dark:divide-gray-600 text-sm z-10 static"
                >
                    <a
                        href="/rework/${leaderboardConfig.rework_id}/users/${user['id']}"
                        class="block px-4 py-2 text-gray-900 hover:bg-gray-500 hover:rounded-md hover:bg-opacity-25 dark:text-white"
                    >
                        <div class="flex items-center space-x-4">
                            <div class="flex-shrink-0">
                                <img
                                class="w-10 h-10 rounded-full"
                                src="https://a.akatsuki.pw/${user['id']}"
                                alt=""
                                />
                            </div>
                            <div>
                                <p class="font-semibold">${user['name']}</p>
                            </div>
                        </div>
                    </a>
                </div>
            `)

            if (index != sliced.length - 1) {
                searchResults.append(`
                    <div class="z-10 dark:bg-gray-700 dark:divide-gray-600">
                        <hr class="my-1 h-px bg-gray-200 border-0 dark:bg-gray-800" />
                    </div>
                `)
            }
        })
        return
    })
}
