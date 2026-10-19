%global source0_hash fdc4d318a08cf419ecfbb3e34aa7be345ca5a8f4cacc9cf09fede0b7d4ec6874
Name:           krecipes
Version:        2.1.0
Release:        24%{?dist}
Summary:        Application to manage recipes and shopping-lists
License:        GPL-2.0-or-later
URL:            https://userbase.kde.org/Krecipes
Source0:        http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
Patch100:       krecipes-2.1.0-gcc6.patch
%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api}}
%{?_kde4_version:Requires: kdelibs4%{?_isa} >= %{_kde4_version}}
Requires:       kde-runtime%{?_kde4_version: >= %{_kde4_version}}
Requires:       oxygen-icon-theme
Requires:       hicolor-icon-theme
Requires:       qt4-sqlite
Requires:       qt4-mysql
Requires:       qt4-postgresql
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  kdelibs4-webkit-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  shared-mime-info
BuildRequires:  sqlite-devel
# /oreon:deps
%description
Krecipes is a program that lets you to manage your recipes, create
shopping lists, choose a recipe based on available ingredients and plan
your menu/diet in advance.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P100 -p1 -b .gcc6

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd
make %{?_smp_mflags} -C %{_target_platform}
%install
make install DESTDIR=%{buildroot} -C %{_target_platform}
desktop-file-validate \
  %{buildroot}%{_kde4_datadir}/applications/kde4/%{name}.desktop
%find_lang %{name} --with-kde
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
