%global source0_hash 4a7a38a9ea0f456f8451d21b307bdf59d38a100b9d70a3a8dec492c5adbcff8b

# gcmd plugins uses symbols defined in gcmd binary
%undefine	_strict_symbol_defs_build

%global        EXIV2_REQ             0.14
%global        GLIB_REQ              2.70.0
%global        LIBGSF_REQ            1.14.26
%global        POPPLER_REQ           0.18
%global        TAGLIB_REQ            1.4
%global        UNIQUE_REQ            0.9.3

%global        if_pre                0

%global        use_gcc_strict_sanitize        0

%global        use_release           1
%global        use_gitbare           0

%if 0%{?use_gitbare} < 1
# force
%global        use_release           1
%endif

%global        flagrel               %{nil}
%if            0%{?use_gcc_strict_sanitize} >= 1
%global        flagrel               %{flagrel}.san
%endif

%if 0%{?use_gitbare}
%global        gittardate            20240721
%global        gittartime            1636
%global        gitbaredate           20240719
%global        git_rev               95c732e0bda821f4b1eb437d2bc175acd268c9c6
%global        git_short             %(echo %{git_rev} | cut -c-8)
%global        git_version           %{gitbaredate}git%{git_short}

%global        if_pre                1
%global        clamp_mtime_to_source_date_epoch  0
%endif

%global        shortver              1.18
%global        fullver               %{shortver}.5

%if 0%{?use_release} >= 1
%global        fedoraver             %{fullver}
%endif
%if 0%{?use_gitbare} >= 1
%global        fedoraver             %{fullver}%{?if_pre:~}%{!?if_pre:^}%{git_version}
%endif

Name:          gnome-commander
# Downgrade 3 times, sorry...
Epoch:         4
Version:       %{fedoraver}
Release:       1%{?dist}%{flagrel}
Summary:       A nice and fast file manager for the GNOME desktop
Summary(pl):   Menadżer plików dla GNOME oparty o Norton Commander'a (TM)
Summary(sv):   GNOME Commander är en snabb och smidig filhanderare för GNOME

# Overall	GPL-2.0-or-later
# data/org.gnome.gnome-commander.appdata.xml.in		CC0-1.0
# doc/C/legal.xml	GFDL-1.1-or-later
# SPDX confirmed
License:       GPL-2.0-or-later AND GFDL-1.1-or-later AND CC0-1.0
URL:           http://gcmd.github.io/
%if 0%{?use_release}
Source0:       http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{shortver}/%{name}-%{version}%{?extratag:-%extratag}.tar.xz
%endif
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
Source1:       gnome-commander.sh
# Source0 is created from Source2
Source2:       create-gcmd-git-bare-tarball.sh
Patch1:        gnome-commander-1.6.0-path-fedora-specific.patch

BuildRequires: gcc-c++
%if 0%{?use_gcc_strict_sanitize}
BuildRequires: libasan
BuildRequires: libubsan
%endif

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool

BuildRequires: pkgconfig(exiv2)         >= %{EXIV2_REQ}
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gnome-vfs-2.0)
BuildRequires: pkgconfig(libgsf-1)        >= %{LIBGSF_REQ}
BuildRequires: pkgconfig(poppler-glib)       >= %{POPPLER_REQ}
BuildRequires: pkgconfig(taglib)        >= %{TAGLIB_REQ}
BuildRequires: pkgconfig(unique-1.0)        >= %{UNIQUE_REQ}

BuildRequires: libICE-devel
BuildRequires: libSM-devel

BuildRequires: meson
BuildRequires: flex
BuildRequires: intltool
BuildRequires: yelp-tools

BuildRequires: /usr/bin/git
BuildRequires: /usr/bin/appstream-util

# %%check
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: pkgconfig(gtest)

Requires:         meld
Requires:         gnome-icon-theme-legacy
%if 0%{?fedora} >= 41
BuildRequires: gdk-pixbuf2-modules-extra
Requires:      gdk-pixbuf2-modules-extra%{?_isa}
%endif

%description
GNOME Commander is a nice and fast file manager for the GNOME desktop. 
In addition to performing the basic filemanager functions the program is 
also an FTP-client and it can browse SMB-networks.

%description -l cs
GNOME Commander je pěkný a rychlý správce souborů pro GNOME desktop.
Kromě základních funkcí správy souborů je program také
FTP klient a umí procházet SMB sítěmi.

%description -l pl
GNOME Commander to niewielki i wydajny menadżer plików umożliwiający
wykonywanie za pomocą klawiatury wszystkich standardowych operacji na plikach.
Dostępne są również dodatkowe funkcje jak np. obsługa FTP, czy też obsługa
sieci SMB.

%description -l ru
Быстро работающий файловый менеджер для GNOME. Может выполнять большинство
типовых операций с файлами, умеет обнаруживать изменения, внесенные в файлы
другими программами, и автоматически обновлять отображаемый список файлов.
Поддерживает описания файловых структур в формате DND и кодировки MIME.
Реализует на базовом уровне поддержку FTP через GnomeVFS.

%description -l sv
GNOME Commander är en snabb och smidig filhanderare för GNOME.
Utöver att kunna hantera filer på din egen dator så kan programmet även
ansluta till FTP-servrar och SMB-nätverk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?use_release}
%setup -q

git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -n %{name}-%{fullver}-%{git_version} -T -a 0
git clone ./%{name}.git/
cd %{name}

git checkout -b %{fullver}-fedora %{git_rev}

# Restore timestamps
set +x
echo "Restore timestamps"
git ls-tree -r --name-only HEAD | while read f
do
	unixtime=$(git log -n 1 --pretty='%ct' -- $f)
	touch -d "@${unixtime}" $f
done
set -x

cp -a [A-Z]* ..
cp -a doc ..

cat > GITHASH <<EOF
EOF

cat GITHASH | while read line
do
  commit=$(echo "$line" | sed -e 's|[ \t].*||')
  git cherry-pick $commit
done

%endif

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-maintainer@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

%patch -P1 -p1 -b .path
git commit -m "Apply Fedora specific path configuration" -a
%if 0%{?use_release}
%endif

# Tweak samba detection
sed -i meson.build \
	-e 's|^\(samba = dependency\)|# \1|' \
	-e 's|^\(have_samba = .*\)$|have_samba = true|' \
	%{nil}
git commit -m "Tweak samba detection" -a

# Don't install unneeded files
sed -i doc/meson.build \
	-e '\@install_data@,\@^)$@s|^\(.*\)$|# \1|' \
	%{nil}
git commit -m "Don't install header files, static archives, documentation" -a

%if 0%{?use_gitbare}
pushd ..
%endif

# gzip
#gzip -9 ChangeLog-*

%if 0%{?use_gitbare}
popd
%endif

%build
export BUILD_TOP_DIR=$(pwd)

%set_build_flags
%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export CXX="${CXX} -fsanitize=address -fsanitize=undefined"
%endif

%if 0%{?use_gitbare}
pushd %{name}
%endif

# Install wrapper script, and move binaries to
# %%{_libexecdir}/%%{name}
%meson \
   --bindir=%{_libexecdir}/%{name} \
   %{nil}

%meson_build --ninja-args "-k 0"

%if 0%{?use_gitbare}
popd
%endif

%install
%if 0%{?use_gitbare}
pushd %{name}
%endif

%meson_install

# Install wrapper
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -cpm 0755 %SOURCE1 %{buildroot}%{_bindir}/%{name}

%if 0%{?use_gitbare}
popd
%endif

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.%{name}.appdata.xml

%if 0%{?use_gitbare}
pushd %{name}
%endif

export ASAN_OPTIONS=detect_leaks=0
xvfb-run sh -c \
	"%meson_test -v"

%if 0%{?use_gitbare}
popd
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS
%doc BUGS
%license COPYING
%doc NEWS
%doc README.md
%doc TODO
%doc doc/*.txt

%{_bindir}/*
%{_libexecdir}/%{name}/
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*

%{_datadir}/glib-2.0/schemas/org.gnome.*xml
%dir %{_datadir}/%{name}
#%%{_datadir}/%{name}/*.txt
%{_datadir}/%{name}/icons/

%{_datadir}/applications/org.gnome.%{name}.desktop
%{_metainfodir}/org.gnome.%{name}.appdata.xml

%{_datadir}/help/*/%{name}/

%{_datadir}/icons/hicolor/scalable/apps/%{name}*.svg
%{_datadir}/pixmaps/%{name}/

%changelog
%autochangelog
