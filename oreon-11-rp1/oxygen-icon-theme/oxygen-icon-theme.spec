%global base_name oxygen-icons

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    oxygen-icon-theme
Summary: Oxygen icon theme
Epoch:   1
Version: 6.1.0
Release:	5%{?dist}

# http://techbase.kde.org/Policies/Licensing_Policy
License: LGPL-3.0-or-later
URL:     https://techbase.kde.org/Projects/Oxygen

Source0: http://download.kde.org/%{stable_kf6}/oxygen-icons/%{base_name}-%{version}.tar.xz
BuildArch: noarch

## upstreamable patches

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel

BuildRequires:  hardlink
# for optimizegraphics
BuildRequires:  kde-dev-scripts
BuildRequires:  kde-filesystem
BuildRequires:  time

# inheritance, though could consider Recommends: if needed -- rex
Requires: hicolor-icon-theme

# upstream names
Provides:       oxygen-icons5 = %{epoch}:%{version}-%{release}
Provides:       oxygen-icons = %{epoch}:%{version}-%{release}
Provides:       kf6-oxygen-icons = %{epoch}:%{version}-%{release}

# some icons moved here from kdepim, add explicit Conflicts to help dep solvers
# http://bugzilla.redhat.com/1308358
Conflicts: kmail < 15.12.2

%description
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
# optimize
pushd %{buildroot}%{_kf6_datadir}/icons/oxygen

du -s  .

hardlink -c -v %{buildroot}%{_kf6_datadir}/icons/oxygen

du -s .

time optimizegraphics

du -s .

## As of 15.04.3, hardlink reports
#Directories 78
#Objects 6926
#IFREG 6848
#Comparisons 901
#Linked 901
#saved 7737344
hardlink -c -v %{buildroot}%{_kf6_datadir}/icons/oxygen

du -s .
popd

# create/own all potential dirs
mkdir -p %{buildroot}%{_kf6_datadir}/icons/oxygen/{16x16,22x22,24x24,32x32,36x36,48x48,64x64,96x96,128x128,512x512,scalable}/{actions,apps,devices,mimetypes,places}


## trigger-based scriptlets
%transfiletriggerin -- %{_datadir}/icons/oxygen
gtk-update-icon-cache --force %{_datadir}/icons/oxygen &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/oxygen
gtk-update-icon-cache --force %{_datadir}/icons/oxygen &>/dev/null || :


%files
%doc AUTHORS CONTRIBUTING
%license COPYING
%{_datadir}/icons/oxygen/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.1.0-4
- Prepare for Oreon 11 (RP1)
