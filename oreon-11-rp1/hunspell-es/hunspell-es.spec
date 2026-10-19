%global source0_hash 03f2616f11de380a28bb9a10cfa957378116a0d1240756e48e3da9e98600abc8
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon} >= 11
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif
Name: hunspell-es
Summary:        Spanish hunspell dictionaries
Version: 25.2.3
Release:        1%{?dist}
Epoch: 1
Source0:        https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
URL: https://cgit.freedesktop.org/libreoffice/dictionaries/tree/es
License: LGPL-3.0-or-later OR GPL-3.0-or-later OR MPL-1.1
BuildArch: noarch
Requires: hunspell-filesystem
Requires: hunspell-es-AR = %{epoch}:%{version}-%{release}
Requires: hunspell-es-BO = %{epoch}:%{version}-%{release}
Requires: hunspell-es-CL = %{epoch}:%{version}-%{release}
Requires: hunspell-es-CO = %{epoch}:%{version}-%{release}
Requires: hunspell-es-CR = %{epoch}:%{version}-%{release}
Requires: hunspell-es-CU = %{epoch}:%{version}-%{release}
Requires: hunspell-es-DO = %{epoch}:%{version}-%{release}
Requires: hunspell-es-EC = %{epoch}:%{version}-%{release}
Requires: hunspell-es-ES = %{epoch}:%{version}-%{release}
Requires: hunspell-es-GT = %{epoch}:%{version}-%{release}
Requires: hunspell-es-GQ = %{epoch}:%{version}-%{release}
Requires: hunspell-es-HN = %{epoch}:%{version}-%{release}
Requires: hunspell-es-MX = %{epoch}:%{version}-%{release}
Requires: hunspell-es-NI = %{epoch}:%{version}-%{release}
Requires: hunspell-es-PA = %{epoch}:%{version}-%{release}
Requires: hunspell-es-PE = %{epoch}:%{version}-%{release}
Requires: hunspell-es-PH = %{epoch}:%{version}-%{release}
Requires: hunspell-es-PR = %{epoch}:%{version}-%{release}
Requires: hunspell-es-PY = %{epoch}:%{version}-%{release}
Requires: hunspell-es-SV = %{epoch}:%{version}-%{release}
Requires: hunspell-es-UY = %{epoch}:%{version}-%{release}
Requires: hunspell-es-US = %{epoch}:%{version}-%{release}
Requires: hunspell-es-VE = %{epoch}:%{version}-%{release}
Supplements: (hunspell and langpacks-es)
# oreon:deps

# /oreon:deps
%description
Spanish (Spain, Mexico, etc.) hunspell dictionaries.

%package        AR
Requires:       hunspell
Summary:        Argentine Spanish hunspell dictionary
%description    AR
Argentine Spanish hunspell dictionary

%package        BO
Requires:       hunspell
Summary:        Bolivian Spanish hunspell dictionary
%description    BO
Bolivian Spanish hunspell dictionary

%package        CL
Requires:       hunspell
Summary:        Chilean Spanish hunspell dictionary
%description    CL
Chilean Spanish hunspell dictionary

%package        CO
Requires:       hunspell
Summary:        Colombian Spanish hunspell dictionary
%description    CO
Colombian Spanish hunspell dictionary

%package        CR
Requires:       hunspell
Summary:        Costa Rican Spanish hunspell dictionary
%description    CR
Costa Rican Spanish hunspell dictionary

%package        CU
Requires:       hunspell
Summary:        Cuban Spanish hunspell dictionary
%description    CU
Cuban Spanish hunspell dictionary

%package        DO
Requires:       hunspell
Summary:        Dominican Spanish hunspell dictionary
%description    DO
Dominican Spanish hunspell dictionary

%package        EC
Requires:       hunspell
Summary:        Ecuadorian Spanish hunspell dictionary
%description    EC
Ecuadorian Spanish hunspell dictionary

%package        ES
Requires:       hunspell
Summary:        European Spanish hunspell dictionary
%description    ES
European Spanish hunspell dictionary

%package        GT
Requires:       hunspell
Summary:        Guatemalan Spanish hunspell dictionary
%description    GT
Guatemalan Spanish hunspell dictionary

%package        GQ
Requires:       hunspell
Summary:        Equatorial Guinean Spanish hunspell dictionary
%description    GQ
Equatorial Guinean Spanish hunspell dictionary

%package        HN
Requires:       hunspell
Summary:        Honduran Spanish hunspell dictionary
%description    HN
Honduran Spanish hunspell dictionary

%package        MX
Requires:       hunspell
Summary:        Mexican Spanish hunspell dictionary
%description    MX
Mexican Spanish hunspell dictionary

%package        NI
Requires:       hunspell
Summary:        Nicaraguan Spanish hunspell dictionary
%description    NI
Nicaraguan Spanish hunspell dictionary

%package        PA
Requires:       hunspell
Summary:        Panamanian Spanish hunspell dictionary
%description    PA
Panamanian Spanish hunspell dictionary

%package        PE
Requires:       hunspell
Summary:        Peruvian Spanish hunspell dictionary
%description    PE
Peruvian Spanish hunspell dictionary

%package        PH
Requires:       hunspell
Summary:        Philippines Spanish hunspell dictionary
%description    PH
Philippines Spanish hunspell dictionary

%package        PR
Requires:       hunspell
Summary:        Puerto Rican Spanish hunspell dictionary
%description    PR
Puerto Rican Spanish hunspell dictionary

%package        PY
Requires:       hunspell
Summary:        Paraguayan Spanish hunspell dictionary
%description    PY
Paraguayan Spanish hunspell dictionary

%package        SV
Requires:       hunspell
Summary:        Salvadoran Spanish hunspell dictionary
%description    SV
Salvadoran Spanish hunspell dictionary

%package        US
Requires:       hunspell
Summary:        US Spanish hunspell dictionary
%description    US
US Spanish hunspell dictionary

%package        UY
Requires:       hunspell
Summary:        Uruguayan Spanish hunspell dictionary
%description    UY
Uruguayan Spanish hunspell dictionary

%package        VE
Requires:       hunspell
Summary:        Venezuelan Spanish hunspell dictionary
%description    VE
Venezuelan Spanish hunspell dictionary

%define es_REGIONS es_AR es_BO es_CL es_CO es_CR es_CU es_DO es_EC es_ES es_GQ es_GT es_HN es_MX es_NI es_PA es_PE es_PH es_PR es_PY es_SV es_US es_UY es_VE

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
for REGION in %{es_REGIONS}; do
    install -pm 0644 dictionaries/es/${REGION}.aff dictionaries/es/${REGION}.dic %{buildroot}%{_datadir}/%{dict_dirname}/
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hunspell-es-AR -f %{oreon_filedir}/hunspell-es-AR.list
%files -n hunspell-es-BO -f %{oreon_filedir}/hunspell-es-BO.list
%files -n hunspell-es-CL -f %{oreon_filedir}/hunspell-es-CL.list
%files -n hunspell-es-CO -f %{oreon_filedir}/hunspell-es-CO.list
%files -n hunspell-es-CR -f %{oreon_filedir}/hunspell-es-CR.list
%files -n hunspell-es-CU -f %{oreon_filedir}/hunspell-es-CU.list
%files -n hunspell-es-DO -f %{oreon_filedir}/hunspell-es-DO.list
%files -n hunspell-es-EC -f %{oreon_filedir}/hunspell-es-EC.list
%files -n hunspell-es-ES -f %{oreon_filedir}/hunspell-es-ES.list
%files -n hunspell-es-GT -f %{oreon_filedir}/hunspell-es-GT.list
%files -n hunspell-es-GQ -f %{oreon_filedir}/hunspell-es-GQ.list
%files -n hunspell-es-HN -f %{oreon_filedir}/hunspell-es-HN.list
%files -n hunspell-es-MX -f %{oreon_filedir}/hunspell-es-MX.list
%files -n hunspell-es-NI -f %{oreon_filedir}/hunspell-es-NI.list
%files -n hunspell-es-PA -f %{oreon_filedir}/hunspell-es-PA.list
%files -n hunspell-es-PE -f %{oreon_filedir}/hunspell-es-PE.list
%files -n hunspell-es-PH -f %{oreon_filedir}/hunspell-es-PH.list
%files -n hunspell-es-PR -f %{oreon_filedir}/hunspell-es-PR.list
%files -n hunspell-es-PY -f %{oreon_filedir}/hunspell-es-PY.list
%files -n hunspell-es-SV -f %{oreon_filedir}/hunspell-es-SV.list
%files -n hunspell-es-US -f %{oreon_filedir}/hunspell-es-US.list
%files -n hunspell-es-UY -f %{oreon_filedir}/hunspell-es-UY.list
%files -n hunspell-es-VE -f %{oreon_filedir}/hunspell-es-VE.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9-4
- Prepare for Oreon 11 (RP1)
