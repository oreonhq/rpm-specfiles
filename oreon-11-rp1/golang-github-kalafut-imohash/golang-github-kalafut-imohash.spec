%global source0_hash 61aef7ceebc7c5cd2cfa6902c4d0be4df3056bf8b776d03005334218a05b460e
%bcond check 0
%global goipath         github.com/kalafut/imohash
Version:                1.0.2
%gometa
%global common_description %{expand:
Fast hashing for large files.}
%global golicenses      LICENSE
%global godocs          README.md algorithm.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Fast hashing for large files
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/imohash-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/twmb/murmur3)
BuildRequires:  golang(gopkg.in/tylerb/is.v1)
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
