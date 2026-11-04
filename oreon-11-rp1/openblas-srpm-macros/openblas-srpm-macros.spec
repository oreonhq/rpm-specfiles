
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
Name:           openblas-srpm-macros
Version:        2
Release:        1%{?dist}
Summary:        OpenBLAS architecture macros
License:        MIT
Source0:        macros.openblas-srpm
BuildArch:      noarch

%description
%{summary}.


%prep
%oreon_sha256



%build


%install
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
mkdir -p %{buildroot}%{macrosdir}
install -m0644 %SOURCE0 %{buildroot}%{macrosdir}/macros.openblas-srpm


%files
%{macrosdir}/macros.openblas-srpm


