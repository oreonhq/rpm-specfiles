%global source0_hash de8c39027373f0b5f4fb9b850c962a172ccb349e41e20c1402faa55b1dd5739c
%global		use_release	0
%global		use_git		0
%global		use_gitbare	1
%if 0%{?use_git} < 1
%if 0%{?use_gitbare} < 1
%global		use_release	1
%endif
%endif
%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}
%if 0%{?use_gitbare}
%global		gittardate		20250325
%global		gittartime		1621
%define		use_gitcommit_as_rel		0
%global		gitbaredate	20250324
%global		git_rev		96e09b05b1897bdca72d8fdfeb1bd8ec68942c42
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif
%if 0%{?use_gitcommit_as_rel}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif
%global		main_version	0.6.4
Name:			lxappearance
Version:		%{main_version}%{git_ver_rpm}
Release:        1%{?dist}
Summary:        Feature-rich GTK+ theme switcher for LXDE
License:		GPL-2.0-or-later
URL:			http://lxde.org/
%if 0%{?use_gitbare}
Source0:        %{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_git}
%endif
%if 0%{?use_release}
%endif
Requires:       lxsession >= 0.4.0
# oreon:deps
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libmenu-cache)
# /oreon:deps
%description
LXAppearance is a new GTK+ theme switcher developed for LXDE, the Lightweight 
X11 Desktop Environment. It is able to change GTK+ themes, icon themes, and 
fonts used by applications. All changes done by the users can be seen 
immediately in the preview area. After clicking the "Apply" button, the 
settings will be written to gtkrc, and all running programs will be asked to 
reload their themes.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains header files for developing plug-ins 
for LXAppearance.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?use_release}
%setup -q -n %{name}-%{main_version}%{git_builddir}

git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T  -n %{name}-%{main_version}%{git_builddir} -a 0
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

cp -a [A-Z]* ..
cp -a data/ ..

cat > GITHASH <<EOF
EOF

cat GITHASH | while read line
do
	commit=$(echo "$line" | sed -e 's|[ \t].*||')
	git cherry-pick $commit
done

%endif

git config user.name "lxpanel Fedora maintainer"
git config user.email "lxpanel-maintainers@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

# Add ACLOCAL_PATH for gettext 0.25 (ref: bug 2366708)
export ACLOCAL_PATH=%{_datadir}/gettext/m4/
sh autogen.sh

%build

%if 0%{?use_gitbare}
pushd %{name}
%endif
%configure \
	--disable-silent-rules \
	--enable-man \
	%{nil}
%make_build
%install
%if 0%{?use_gitbare}
pushd %{name}
%endif
%make_install
%if 0%{?use_gitbare}
popd
%endif
mkdir -p %{buildroot}%{_libdir}/%{name}/plugins/
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n lxappearance-devel -f %{oreon_filedir}/lxappearance-devel.list

%changelog

%autochangelog
