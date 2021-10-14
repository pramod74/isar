# @pytest.mark.parametrize(
#     "mission_id, mock_get_mission, mock_get_mission_side_effect,"
#     "mock_ready_to_start, mock_start, expected_output, expected_status_code",
#     [
#         (
#             12345,
#             mock_mission_definition(),
#             None,
#             mock_ready_to_start_mission(HTTPStatus.OK),
#             mock_start_mission(HTTPStatus.OK),
#             StartMissionMessages.success(),
#             HTTPStatus.OK,
#         ),
#         (
#             12345,
#             None,
#             RequestException,
#             mock_ready_to_start_mission(HTTPStatus.OK),
#             mock_start_mission(HTTPStatus.OK),
#             StartMissionMessages.mission_not_found(),
#             HTTPStatus.NOT_FOUND,
#         ),
#     ],
# )
# def test_start_mission(
#     client,
#     access_token,
#     mocker,
#     mission_id,
#     mock_get_mission,
#     mock_get_mission_side_effect,
#     mock_ready_to_start,
#     mock_start,
#     expected_output,
#     expected_status_code,
# ):
#     mocker.patch.object(
#         EchoPlanner,
#         "get_mission",
#         return_value=mock_get_mission,
#         side_effect=mock_get_mission_side_effect,
#     )
#     mocker.patch.object(
#         SchedulingUtilities,
#         "ready_to_start_mission",
#         return_value=mock_ready_to_start,
#     )
#     mocker.patch.object(
#         SchedulingUtilities,
#         "start_mission",
#         return_value=mock_start,
#     )
#
#     response = client.get(
#         "/schedule/start-echo-mission",
#         headers={"Authorization": "Bearer {}".format(access_token)},
#         query_string={"mission_id": mission_id},
#     )
#     assert response.json == asdict(expected_output)
#     assert response.status_code == expected_status_code
