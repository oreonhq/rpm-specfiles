%global source0_hash d51d934afee3e2306881439028dd4115167d261b5e4de5a930897fefe2e5b8a3
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/smartystreets/goconvey
Version:                1.8.1
%gometa
%global common_description %{expand:
GoConvey, a yummy Go testing tool for gophers. Works with go test. Use it in the
terminal or browser according to your viewing pleasure.
Features:
 - Directly integrates with go test
 - Fully-automatic web UI (works with native Go tests, too)
 - Huge suite of regression tests
 - Shows test coverage (Go 1.2+)
 - Readable, colorized console output (understandable by any manager, IT or not)
 - Test code generator
 - Desktop notifications (optional)
 - Immediately open problem lines in Sublime Text (some assembly required)}
%global golicenses      LICENSE.md web/client/resources/fonts/Open_Sans/LICENSE.txt web/client/resources/fonts/Orbitron/OFL.txt
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go testing in the browser
License:        LicenseRef-Callaway-MIT AND Apache-2.0 AND LicenseRef-Callaway-OFL
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/goconvey-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/jtolds/gls)
BuildRequires:  golang(github.com/smartystreets/assertions)
BuildRequires:  golang(golang.org/x/tools/go/packages)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d web/server/watch -d web/server/system
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
