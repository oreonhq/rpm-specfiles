%global source0_hash none

Name:    kdepim
Summary: KDE Personal Information Metapackage
Epoch:   7
Version: 17.12.3
Release: 19%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://community.kde.org/KDE_PIM

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

Requires: %{name}-common = %{epoch}:%{version}-%{release}

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
Requires: akregator >= %{majmin_ver}
Requires: kaddressbook >= %{majmin_ver}
Requires: kalarm >= %{majmin_ver}
Requires: knotes >= %{majmin_ver}
Requires: kmail >= %{majmin_ver}
# kontact already pulls in kaddressbook, kmail, korganizer
Requires: kontact >= %{majmin_ver}
Requires: korganizer >= %{majmin_ver}

BuildRequires:  kf5-rpm-macros

%description
%{summary}, including:
* akregator: feed aggregator
* blogilo: blogging application, focused on simplicity and usability}
* kmail: email client
* knotes: sticky notes for the desktop
* kontact: integrated PIM management
* korganizer: journal, appointments, events, todos

%package        common
Summary:        Common  files for %{name}
Obsoletes:      kdepim-libs < 7:16.12
%description    common
%{summary}.

%prep
# blank

%build
# blank

%install
# blank

%files
# empty

%files common 
# empty

%changelog
%autochangelog
