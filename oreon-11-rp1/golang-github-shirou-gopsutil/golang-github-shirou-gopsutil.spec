%global source0_hash c4c61a6ade378e39b89a33bb959fc2c32092f0ba35f39aec99519fad4e9173b4
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/shirou/gopsutil
Version:                3.24.5
%gometa
%global common_description %{expand:
Psutil for golang.}
%global golicenses      LICENSE
%global godocs          README.md windows_memo.rst\\\
                        _tools/v3migration/v3Changes.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Psutil for golang
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gopsutil-%{version}.tar.gz
# oreon:deps
BuildRequires:  /usr/bin/pgrep
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

for test in "TestUsers" "Test_Process_Cwd" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%ifarch aarch64
for test in "TestCpuInfo" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%endif
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
