%global source0_hash none

Name:           icc-profiles-basiccolor-printing2009
Version:        1.2.0
Release:        27%{?dist}
Summary:        The OpenICC profiles from basICColor

License:        zlib
URL:            http://www.freedesktop.org/wiki/OpenIcc
Source0:        http://downloads.sourceforge.net/project/openicc/basICColor-Profiles/%{name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  color-filesystem
BuildRequires: make
Requires:       color-filesystem
#Owns %%{_icccolordir}/basICColor
Requires:       icc-profiles-openicc

%description
Printing profiles according to ISO 12647-2. These are CMYK
ICC profiles for ISO Printing conditions.

%prep
%setup -q

%build
%configure --enable-verbose
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING
%{_icccolordir}/basICColor/ISOcoated_v2_300_bas.ICC
%{_icccolordir}/basICColor/ISOcoated_v2_bas.ICC
%{_icccolordir}/basICColor/ISOcoated_v2_grey1c_bas.ICC
%{_icccolordir}/basICColor/ISOnewspaper_v4_26_bas.ICC
%{_icccolordir}/basICColor/ISOuncoatedyellowish_bas.ICC
%{_icccolordir}/basICColor/PSO_Coated_300_NPscreen_ISO12647_bas.ICC
%{_icccolordir}/basICColor/PSO_Coated_NPscreen_ISO12647_bas.ICC
%{_icccolordir}/basICColor/PSO_LWC_Improved_bas.ICC
%{_icccolordir}/basICColor/PSO_LWC_Standard_bas.ICC
%{_icccolordir}/basICColor/PSO_MFC_Paper_bas.ICC
%{_icccolordir}/basICColor/PSO_SNP_Paper_bas.ICC
%{_icccolordir}/basICColor/PSO_Uncoated_ISO12647_bas.ICC
%{_icccolordir}/basICColor/PSO_Uncoated_NPscreen_ISO12647_bas.ICC
%{_icccolordir}/basICColor/SC_paper_bas.ICC

%changelog
%autochangelog
