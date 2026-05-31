%global source0_hash none

Name:           rpm-mpi-hooks
Version:        8
Release:        13%{?dist}
Summary:        RPM dependency generator hooks for MPI packages

License:        MIT
BuildArch:      noarch

Source0:        mpi.attr
Source1:        mpilibsymlink.attr
Source2:        mpi.prov
Source3:        mpi.req
Source4:        LICENSE

Requires:       filesystem
# Instead of adding a BuildRequires to every MPI implementation spec
Requires:       environment-modules

%description
RPM dependency generator hooks for MPI packages. This package should be added
as a BuildRequires to all mpi implementations (i.e. openmpi, mpich) as well as
a Requires to the their -devel packages.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }cp -a %SOURCE4 .


%build
# Nothing to build


%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/fileattrs/mpi.attr
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/fileattrs/mpilibsymlink.attr
install -Dpm 0755 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/mpi.prov
install -Dpm 0755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/mpi.req


%files
%license LICENSE
%{_rpmconfigdir}/fileattrs/mpi.attr
%{_rpmconfigdir}/fileattrs/mpilibsymlink.attr
%{_rpmconfigdir}/mpi.req
%{_rpmconfigdir}/mpi.prov


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8-13
- Prepare for Oreon 11 (RP1)
