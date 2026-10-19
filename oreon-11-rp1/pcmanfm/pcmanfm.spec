%global source0_hash 31ec1d013fc12b8bdb50539f6118bd6d748f0314bc4790cdd17d6ce3b8dd5bb7
%global		use_release	0
%global		use_gitbare	1
%if 0%{?use_gitbare} < 1
%global		use_release	1
%endif
%global		main_version	1.4.0
%undefine		prever
%global		prerpmver		%(echo "%{?prever}" | sed -e 's|-||g')
%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}
%if 0%{?use_gitbare} >= 1
%global		tarballdate	20251218
%global		tarballtime	1224
%define		use_gitcommit_as_rel		1
%global		githeaddate	20251022
%global		git_rev		09087446392d08c25412cade107bdec0a6e8ae7b
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{githeaddate}git%{git_short}
%endif
%global		libfm_minver	1.4.0
%undefine		_changelog_trimtime
%if 0%{?use_gitbare}
%if 0%{?use_gitcommit_as_rel}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif
%endif
%global		use_gcc_strict_sanitize	0
%global		flagrel	%{nil}
%if	0%{?use_gcc_strict_sanitize} >= 1
%global		flagrel	%{flagrel}.san
%endif
Name:		pcmanfm
Version:	%{main_version}%{git_ver_rpm}
Release:        2%{?dist}
Summary:        Extremly fast and lightweight file manager
License:	GPL-2.0-or-later
URL:		http://pcmanfm.sourceforge.net/
%if 0%{?use_gitbare} >= 1
Source0:        %{name}-%{tarballdate}T%{tarballtime}.tar.gz
%endif
%if 0%{?use_release} >= 1
%endif
Source1:	pcmanfm.desktop.in
Source2:	pcmanfm-desktop-pref.desktop.in
Source100:	create-pcmanfm-git-bare-tarball.sh
Patch101:	pcmanfm-0101-split-out-per-monitor-initialization-part-from-fm_de.patch
Patch102:	pcmanfm-0102-use-GList-for-FmDesktop-entries-instead-of-static-ar.patch
Patch103:	pcmanfm-0103-Fix-the-bug-that-desktop-configuration-is-not-proper.patch
Patch104:	pcmanfm-0104-Finish-implementation-of-inserting-new-monitor.patch
Patch202:	pcmanfm-0202-connect_model-connect-to-signal-before-setting-folde.patch
%if 0%{?use_gitbare}
%endif
%if 0%{?use_gcc_strict_sanitize}
%endif
Requires:		libfm-gtk-utils
Requires:	libfm >= %{libfm_minver}
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  intltool
BuildRequires:  libfm-gtk-devel
BuildRequires:  make
BuildRequires:  menu-cache-devel
# /oreon:deps
%description
PCMan File Manager is an extremly fast and lightweight file manager 
which features tabbed browsing and user-friendly interface.

%package		devel
Summary:		Development files for %{name}
Requires:		%{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?use_release}
%setup -q -n %{name}-%{main_version}%{?prever}%{git_builddir}
#install -cpm 644 %{SOURCE1} %{SOURCE2} data/

git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T -n %{name}-%{main_version}%{?prever}%{git_builddir}%{?prever} -a 0
git clone ./%{name}.git/
cd %{name}

#git checkout -b %{version}-fedora %{version}
git checkout -b %{main_version}-fedora %{git_rev}

# Restore timestamps
set +x
echo "Restore timestamps"
git ls-tree -r --name-only HEAD | while read f
do
	unixtime=$(git log -n 1 --pretty='%ct' -- $f)
	touch -d "@${unixtime}" $f
done
set -x

install -cpm 0644  [A-Z]* ..
%endif

git config user.name "pcmanfm Fedora maintainer"
git config user.email "pcmanfm-owner@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -q -m "init tree"
%endif

cat %PATCH101 | git am
cat %PATCH102 | git am
cat %PATCH103 | git am
cat %PATCH104 | git am
cat %PATCH202 | git am

%if 0%{?use_gitbare}
# Add ACLOCAL_PATH for gettext 0.25 (ref: bug 2366708)
export ACLOCAL_PATH=%{_datadir}/gettext/m4/
# Patch0
autoreconf -fi
%endif

# permission fix
%if 0%{?use_gitbare} < 1
chmod 0644 [A-Z]*
%endif
# ??
chmod u+x configure
chmod u+x */

%build

%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export CXX="${CXX} -fsanitize=address -fsanitize=undefined"
export LDFLAGS="${LDFLAGS} -pthread"
%endif
%if 0%{?use_gitbare}
cd %{name}
%endif
export LDFLAGS="-lm"
%configure \
	--disable-silent-rules \
	--with-gtk=3
make -C po -j1 GMSGFMT="msgfmt --statistics"
make  %{?_smp_mflags} -k
%install
%if 0%{?use_gitbare}
cd %{name}
%endif
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p"
desktop-file-install \
	--delete-original \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--remove-category 'Application' \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}*.desktop
%if 0%{?use_gitbare}
cd ..
%endif
%find_lang %{name}
%{_prefix}/lib/rpm/check-rpaths
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n pcmanfm-devel -f %{oreon_filedir}/pcmanfm-devel.list

%changelog

%autochangelog
