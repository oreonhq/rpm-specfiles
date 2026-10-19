%global source0_hash 795d7febcf73503bca2ac9806f12ff6b33b47c13eef2d50b81b10e241d9bdb22
%bcond check 0
%global goipath         mvdan.cc/xurls
%global forgeurl        https://github.com/mvdan/xurls
Version:                2.2.0
%gometa
%global goaltipaths     github.com/mvdan/xurls mvdan.cc/xurls/v2
%global common_description %{expand:
Extract urls from text using regular expressions. Requires Go 1.10.3 or later.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Extract urls from text
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/xurls-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/rogpeppe/go-internal/testscript)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d cmd/xurls
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
