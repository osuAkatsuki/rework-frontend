var scoreTable = $("#profile-scores")
var spinningCircle = $("#spinning-empty-circle")

$(document).ready(function () {
    loadScores()
})


function loadScores() {
    fetch(`/api/v1/scores/${profileConfig.user_id}?` + new URLSearchParams({
        rework_id: profileConfig.rework_id,
    }))
    .then(response => response.json())
    .then(data => {
        if (data.data.length === 0) {
            scoreTable.append(`
            <tr class="border-b border-gray-200 dark:border-gray-700">
                <td colspan="9" class="w-full h-full py-4 px-6 bg-gray-50 dark:bg-gray-800">
                    <div class="flex justify-center">
                        <div class="inline dark:text-white text-2xl">
                            No scores found :(
                        </div>
                    </div>
                </td>
            </tr>
            `)
            spinningCircle.remove()
            return
        }

        data.data.forEach(score => {
            scoreTable.append(`
                <tr class="border-b border-gray-200 dark:border-gray-700">
                    <td class="py-4 px-6 dark:bg-gray-700 whitespace-nowrap">
                        #${numberCommas(score['new_rank'])}
                        <br />
                        ${renderDelta(score['old_rank'], score['new_rank'])}
                    </td>
                    <td class="py-4 px-6 bg-gray-50 dark:bg-gray-800">
                        #${numberCommas(score['old_rank'])}
                    </td>
                    <td class="py-2 px-4 dark:bg-gray-700">
                        <a href="https://akatsuki.pw/beatmaps/${score['beatmap']['id']}">
                            <img
                                src="https://assets.ppy.sh/beatmaps/${score['beatmap']['set_id']}/covers/list.jpg"
                                class="h-12 w-20 object-cover rounded-md object-cover inline-block"
                            />
                            ${score['beatmap']['song_name']}
                        </a>
                    </td>
                    <td class="py-4 px-6 bg-gray-50 dark:bg-gray-800">
                        ${getScoreMods(score['mods'])}
                    </td>
                    <td class="py-4 px-6 dark:bg-gray-700 whitespace-nowrap">
                        ${numberCommas(score['new_pp'])}pp
                        <br />
                        ${renderDelta(score['new_pp'], score['old_pp'])}
                    </td>
                    <td class="py-4 px-6 bg-gray-50 dark:bg-gray-800">
                        ${numberCommas(score['old_pp'])}pp
                    </td>
                    <td class="py-4 px-6 dark:bg-gray-700">${score['accuracy'].toFixed(2)}%</td>
                    <td class="py-4 px-6 bg-gray-50 dark:bg-gray-800">
                        ${numberCommas(score['max_combo'])}x
                    </td>
                    <td class="py-4 px-6 dark:bg-gray-700">
                        ${numberCommas(score['nmiss'])}x
                    </td>
                </tr>
            `)
        })
        spinningCircle.remove()
    })
}
