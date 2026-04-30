
Name:    kde-baseapps
Summary: KDE Core Applications 
Version: 16.12.2
Release: 22%{?dist}

# Automatically converted from old format: GPLv2 and GFDL - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-GFDL
URL:     http://kde.org/
BuildArch: noarch

Obsoletes: kdebase < 6:4.7.97-10
#Provides: kdebase = 6:%%{version}-%%{release}

Obsoletes: kdebase4 < %{version}-%{release}
#Provides: kdebase4 = %%{version}-%%{release}

Requires: %{name}-common = %{version}-%{release}

Requires: kdialog >= %{version}
Requires: keditbookmarks >= %{version}
Requires: kfind >= %{version}
%ifarch %{?qt5_qtwebengine_arches}%{?!qt5_qtwebengine_arches:%{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}
Requires: konqueror >= %{version}
%endif

%description
Metapackage for Core KDE applications.

%package common
Summary: Common files for %{name}
#Conflicts: kde-baseapps < 4.12.0-2
Obsoletes: dolphin4 < 16.12
Obsoletes: dolphin4-libs < 16.12
Obsoletes: kde-baseapps-libs < 16.12
Obsoletes: kde-baseapps-devel < 16.12
Obsoletes: kde-plasma-folderview = 6:16.12
Obsoletes: kdepasswd < 16.12
Obsoletes: libkonq < 16.12
%description common
%{summary}


%prep
# blank


%build
# blank


%install
#blank


%files
# empty metapackage

%files common
# empty


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 16.12.2-22
- Prepare for Oreon 11 (RP1)
