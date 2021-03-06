#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-docker-engine-api
Version  : 6156954c5d57a1728c65593b13f50c405d9de9ed
Release  : 6
URL      : https://github.com/docker/engine-api/archive/6156954c5d57a1728c65593b13f50c405d9de9ed.tar.gz
Source0  : https://github.com/docker/engine-api/archive/6156954c5d57a1728c65593b13f50c405d9de9ed.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : go

%description
[![GoDoc](https://godoc.org/github.com/docker/engine-api?status.svg)](https://godoc.org/github.com/docker/engine-api)

%prep
%setup -q -n engine-api-6156954c5d57a1728c65593b13f50c405d9de9ed

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/docker/engine-api"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x github.com/docker/engine-api

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/docker/engine-api/client/client.go
/usr/lib/golang/src/github.com/docker/engine-api/client/client_darwin.go
/usr/lib/golang/src/github.com/docker/engine-api/client/client_mock_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/client_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/client_unix.go
/usr/lib/golang/src/github.com/docker/engine-api/client/client_windows.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_attach.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_commit.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_commit_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_copy.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_create.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_create_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_diff.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_diff_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_exec.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_exec_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_export.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_export_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_inspect.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_inspect_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_kill.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_kill_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_list.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_list_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_logs.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_logs_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_pause.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_pause_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_remove.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_remove_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_rename.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_rename_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_resize.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_resize_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_restart.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_restart_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_start.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_start_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_stats.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_stats_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_stop.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_stop_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_top.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_top_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_unpause.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_unpause_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_update.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_update_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_wait.go
/usr/lib/golang/src/github.com/docker/engine-api/client/container_wait_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/errors.go
/usr/lib/golang/src/github.com/docker/engine-api/client/events.go
/usr/lib/golang/src/github.com/docker/engine-api/client/hijack.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_build.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_build_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_create.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_create_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_history.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_history_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_import.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_import_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_inspect.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_inspect_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_list.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_list_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_load.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_load_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_pull.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_push.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_remove.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_remove_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_save.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_save_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_search.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_tag.go
/usr/lib/golang/src/github.com/docker/engine-api/client/image_tag_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/info.go
/usr/lib/golang/src/github.com/docker/engine-api/client/info_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/interface.go
/usr/lib/golang/src/github.com/docker/engine-api/client/login.go
/usr/lib/golang/src/github.com/docker/engine-api/client/network_connect.go
/usr/lib/golang/src/github.com/docker/engine-api/client/network_connect_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/network_create.go
/usr/lib/golang/src/github.com/docker/engine-api/client/network_create_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/network_disconnect.go
/usr/lib/golang/src/github.com/docker/engine-api/client/network_disconnect_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/network_inspect.go
/usr/lib/golang/src/github.com/docker/engine-api/client/network_inspect_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/network_list.go
/usr/lib/golang/src/github.com/docker/engine-api/client/network_list_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/network_remove.go
/usr/lib/golang/src/github.com/docker/engine-api/client/network_remove_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/privileged.go
/usr/lib/golang/src/github.com/docker/engine-api/client/request.go
/usr/lib/golang/src/github.com/docker/engine-api/client/transport/cancellable/canceler.go
/usr/lib/golang/src/github.com/docker/engine-api/client/transport/cancellable/canceler_go14.go
/usr/lib/golang/src/github.com/docker/engine-api/client/transport/cancellable/cancellable.go
/usr/lib/golang/src/github.com/docker/engine-api/client/transport/client.go
/usr/lib/golang/src/github.com/docker/engine-api/client/transport/transport.go
/usr/lib/golang/src/github.com/docker/engine-api/client/version.go
/usr/lib/golang/src/github.com/docker/engine-api/client/volume_create.go
/usr/lib/golang/src/github.com/docker/engine-api/client/volume_create_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/volume_inspect.go
/usr/lib/golang/src/github.com/docker/engine-api/client/volume_inspect_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/volume_list.go
/usr/lib/golang/src/github.com/docker/engine-api/client/volume_list_test.go
/usr/lib/golang/src/github.com/docker/engine-api/client/volume_remove.go
/usr/lib/golang/src/github.com/docker/engine-api/client/volume_remove_test.go
/usr/lib/golang/src/github.com/docker/engine-api/doc.go
/usr/lib/golang/src/github.com/docker/engine-api/types/auth.go
/usr/lib/golang/src/github.com/docker/engine-api/types/blkiodev/blkio.go
/usr/lib/golang/src/github.com/docker/engine-api/types/client.go
/usr/lib/golang/src/github.com/docker/engine-api/types/configs.go
/usr/lib/golang/src/github.com/docker/engine-api/types/container/config.go
/usr/lib/golang/src/github.com/docker/engine-api/types/container/host_config.go
/usr/lib/golang/src/github.com/docker/engine-api/types/container/hostconfig_unix.go
/usr/lib/golang/src/github.com/docker/engine-api/types/container/hostconfig_windows.go
/usr/lib/golang/src/github.com/docker/engine-api/types/events/events.go
/usr/lib/golang/src/github.com/docker/engine-api/types/filters/parse.go
/usr/lib/golang/src/github.com/docker/engine-api/types/filters/parse_test.go
/usr/lib/golang/src/github.com/docker/engine-api/types/network/network.go
/usr/lib/golang/src/github.com/docker/engine-api/types/registry/registry.go
/usr/lib/golang/src/github.com/docker/engine-api/types/seccomp.go
/usr/lib/golang/src/github.com/docker/engine-api/types/stats.go
/usr/lib/golang/src/github.com/docker/engine-api/types/strslice/strslice.go
/usr/lib/golang/src/github.com/docker/engine-api/types/strslice/strslice_test.go
/usr/lib/golang/src/github.com/docker/engine-api/types/time/timestamp.go
/usr/lib/golang/src/github.com/docker/engine-api/types/time/timestamp_test.go
/usr/lib/golang/src/github.com/docker/engine-api/types/types.go
/usr/lib/golang/src/github.com/docker/engine-api/types/versions/v1p19/types.go
/usr/lib/golang/src/github.com/docker/engine-api/types/versions/v1p20/types.go
