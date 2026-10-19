%global source0_hash a5159175a7faa006a187ce617679e689ed5951401f54de536a4237d821e8f505
%bcond check 0
%global goipath         github.com/pquerna/ffjson
%global commit          aa0246cd15f76c96de6b96f22a305bdfb2d1ec02
%gometa
%global common_description %{expand:
Ffjson generates static MarshalJSON and UnmarshalJSON functions for structures
in Go. The generated functions reduce the reliance upon runtime reflection to do
serialization and are generally 2 to 3 times faster. In cases where ffjson
doesn't understand a Type involved, it falls back to encoding/json, meaning it
is a safe drop in replacement. By using ffjson your JSON serialization just gets
faster with no additional code changes.}
%global golicenses      LICENSE NOTICE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Faster JSON serialization for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/ffjson-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
rm -rf tests/types/ff

%build

%gobuild -o %{gobuilddir}/bin/ffjson %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d tests
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
