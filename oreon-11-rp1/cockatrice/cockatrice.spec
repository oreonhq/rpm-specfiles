%global source0_hash 73cabec34604261b3ec2beb66b6a11faff0b0d1ca50f25cc58a45325a39225d4
%global		gittag0			2025-04-03-Release-2.10.2
%define			lang_subpkg() \
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  protobuf-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtwebsockets-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
# /oreon:deps
%package		langpack-%{1}\
Summary:		%{2} language data for %{name}\
BuildArch:	noarch\
Requires:		%{name} = %{version}-%{release}\
Supplements:	(%{name} = %{version}-%{release} and langpacks-%{1})\
\
%description	langpack-%{1}\
%{2} language data for %{name}.\
\
%description
Cockatrice is an open-source multi-platform supported program for playing
tabletop card games over a network. The program's server design prevents any
kind of client modifications to gain an unfair advantage in a game.
The client also has a built in single-player mode where you can create decks
without being connected to a server.

%package server
Summary:	Standalone server for Cockatrice
Provides:	servatrice = %{version}-%{release}
Requires:	%{name}-utils = %{version}-%{release}
%description server
Cockatrice is an open-source multi-platform supported program for playing
tabletop card games over a network. The program's server design prevents any
kind of client modifications to gain an unfair advantage in a game.
The client also has a built in single-player mode where you can create decks
without being connected to a server.

This is the standalone server, "servatrice".

%package utils
Summary:	Utilities common to both cockatrice and servatrice
%description utils
Cockatrice is an open-source multi-platform supported program for playing
tabletop card games over a network. The program's server design prevents any
kind of client modifications to gain an unfair advantage in a game.
The client also has a built in single-player mode where you can create decks
without being connected to a server.

This package provides utilities required by both cockatrice and servatrice.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cockatrice-%{gittag0}
%patch -P 0
find . -iname "*.h" -exec chmod a-x "{}" \;
find . -iname "*.cpp" -exec chmod a-x "{}" \;
# The API for Protobuf v4 (23.x) requires at least C++14. When compiled as
# C++17, abseil-cpp (a transitive dependency via the generated bindings)
# requires API users to compile with at least C++17.
sed -r -i 's/(CMAKE_CXX_STANDARD )11\b/\117/' CMakeLists.txt

%build

%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS=OFF \
	-DWITH_SERVER=ON
%cmake_build
%check

appstream-util validate-relax --nonet %{SOURCE1}
desktop-file-validate cockatrice/%{name}.desktop
desktop-file-validate servatrice/servatrice.desktop
desktop-file-validate oracle/oracle.desktop
%install
%cmake_install
install -m644 -D %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
rm %{buildroot}%{_datadir}/%{name}/translations/%{name}_en@pirate.qm
rm %{buildroot}%{_datadir}/oracle/translations/oracle_en@pirate.qm
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n cockatrice-server -f %{oreon_filedir}/cockatrice-server.list
%files -n cockatrice-utils -f %{oreon_filedir}/cockatrice-utils.list
%files -n cockatrice-langpack-cs -f %{oreon_filedir}/cockatrice-langpack-cs.list
%files -n cockatrice-langpack-de -f %{oreon_filedir}/cockatrice-langpack-de.list
%files -n cockatrice-langpack-en_US -f %{oreon_filedir}/cockatrice-langpack-en_US.list
%files -n cockatrice-langpack-es -f %{oreon_filedir}/cockatrice-langpack-es.list
%files -n cockatrice-langpack-et -f %{oreon_filedir}/cockatrice-langpack-et.list
%files -n cockatrice-langpack-fr -f %{oreon_filedir}/cockatrice-langpack-fr.list
%files -n cockatrice-langpack-it -f %{oreon_filedir}/cockatrice-langpack-it.list
%files -n cockatrice-langpack-ja -f %{oreon_filedir}/cockatrice-langpack-ja.list
%files -n cockatrice-langpack-ko -f %{oreon_filedir}/cockatrice-langpack-ko.list
%files -n cockatrice-langpack-nb -f %{oreon_filedir}/cockatrice-langpack-nb.list
%files -n cockatrice-langpack-nl -f %{oreon_filedir}/cockatrice-langpack-nl.list
%files -n cockatrice-langpack-pl -f %{oreon_filedir}/cockatrice-langpack-pl.list
%files -n cockatrice-langpack-pt -f %{oreon_filedir}/cockatrice-langpack-pt.list
%files -n cockatrice-langpack-pt_BR -f %{oreon_filedir}/cockatrice-langpack-pt_BR.list
%files -n cockatrice-langpack-ru -f %{oreon_filedir}/cockatrice-langpack-ru.list
%files -n cockatrice-langpack-sr -f %{oreon_filedir}/cockatrice-langpack-sr.list
%files -n cockatrice-langpack-sv -f %{oreon_filedir}/cockatrice-langpack-sv.list
%files -n cockatrice-langpack-zh-Hans -f %{oreon_filedir}/cockatrice-langpack-zh-Hans.list

%changelog

%autochangelog
