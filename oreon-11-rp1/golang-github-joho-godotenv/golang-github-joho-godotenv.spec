%global source0_hash f87c261109efd54c8f16b40252e820d690af571975c25247d2438c43be0be4a1
%bcond check 0
%global goipath         github.com/joho/godotenv
Version:                1.5.1
%gometa
%global common_description %{expand:
A Go (golang) port of the Ruby dotenv project (which loads env vars from a .env
file).}
%global golicenses      LICENCE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go port of Ruby's dotenv library
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/godotenv-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
