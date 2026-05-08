Name:           gnat-srpm-macros
Version:        7
Release:        %autorelease
Summary:        RPM macros needed when source packages that need GNAT are built
Summary(sv):    RPM-makron som behövs när källkodspaket som behöver GNAT byggs

License:        FSFAP
URL:            https://gcc.gnu.org/wiki/GNAT

Source0:        macros.gnat-srpm

BuildArch:      noarch

%description
This package contains RPM macros that need to be available when source RPM
packages that need the GNAT tools are built. It is a standalone package in
order to have as few dependencies as possible.

%description -l sv
Det här paketet innehåller RPM-makron som behöver finnas tillgängliga när käll-
RPM-paket som behöver GNAT-verktygen byggs. Det är ett fristående paket för att
bero av så få andra paket som möjligt.

%install
install -Dpm0644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.gnat-srpm

%files
%{_rpmmacrodir}/macros.gnat-srpm

%changelog
* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7-1
- Import from Fedora 44 dist-git, debrand URL and macro comments, replace changelog
