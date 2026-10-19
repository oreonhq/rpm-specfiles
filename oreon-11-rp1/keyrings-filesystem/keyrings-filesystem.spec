%global source0_hash none
Name:           keyrings-filesystem
Version:        1
Release:        1%{?dist}
Summary:        Keyrings filesystem layout
License:        LicenseRef-Fedora-Public-Domain
BuildArch:      noarch
Requires:       filesystem
Requires:       rpm
# oreon:deps

# /oreon:deps
%description
This package provides the directory to store keyrings.

%prep

# Nothing to prep

%build

%install
install -d %{buildroot}%{_rpmconfigdir}/macros.d
install -d %{buildroot}%{_datadir}/keyrings
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.keyrings <<EOF
%%_keyringsdir %%_datadir/keyrings
EOF
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
