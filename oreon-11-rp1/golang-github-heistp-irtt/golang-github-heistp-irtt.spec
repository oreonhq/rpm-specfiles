%global source0_hash 796538208275798b9bd7a9b4c1565a9590999c3db711e38026f2bd21f00b43ef
%bcond check 0
%global goipath         github.com/heistp/irtt
Version:                0.9.1
%gometa
%global common_description %{expand:
Isochronous Round-Trip Tester.}
%global golicenses      LICENSE
%global godocs          CHANGES.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Isochronous Round-Trip Tester
License:        GPL-2.0-only
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/irtt-%{version}.tar.gz
Patch: irtt-pflag.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0644 -vp %{gosourcedir}/doc/*.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
