%global source0_hash 0a01d2b131419cb2b9f7d910a2c90b824449bd91005b47efb235dc707665337a
%bcond check 0
%global goipath         github.com/denisbrodbeck/machineid
Version:                1.0.1
%gometa
%global common_description %{expand:
Get the unique machine id of any host (without admin privileges).}
%global golicenses      LICENSE.md
%global godocs          README.md logo.png
Name:           %{goname}
Release:        1%{?dist}
Summary:        Get the unique machine id of any host (without admin privileges)
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/machineid-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%package -n     machineid
Summary:        Get the unique machine id of any host (without admin privileges)
%description -n machineid
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
%oreon_autofiles machineid usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n machineid -f %{oreon_filedir}/machineid.list

%changelog

%autochangelog
