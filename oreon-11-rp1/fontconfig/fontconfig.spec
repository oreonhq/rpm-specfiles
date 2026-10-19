%global source0_hash 4f7b554a38cdf78c033f666c8871f3749e14a094f65a07f630c91ed0b43d35e3
%global freetype_version 2.9.1
Summary:        Font configuration and customization library
Name:		fontconfig
Version:	2.18.3
Release:        1%{?dist}
License:	HPND AND LicenseRef-Fedora-Public-Domain AND Unicode-DFS-2016
Source0:        https://src.fedoraproject.org/repo/pkgs/fontconfig/fontconfig-2.18.3.tar.xz/sha512/c3e769f74dc21093ada48084bddaca1ab525b1c4f04c5c11f067b69346fab153cad95de8b8238b20b02e8b9679c314bf2e0e9c4218511d8fe0f1826e4c4c6a24/fontconfig-2.18.3.tar.xz
URL:		http://fontconfig.org
Source1:	25-no-bitmap-fedora.conf
Source2:	fc-cache
Patch0:		%{name}-sleep-less.patch
Patch4:		%{name}-drop-lang-from-pkgkit-format.patch
Patch6:		%{name}-lower-nonlatin-conf.patch
Requires:	fonts-filesystem freetype
Requires(pre):    xml-common
Requires(postun): xml-common
Requires(pre):	freetype >= 2.9.1-6
Requires(post):	grep coreutils
Requires:	font(:lang=en)
Suggests:	font(notosans)
# oreon:deps
BuildRequires:  docbook-utils
BuildRequires:  docbook-utils-pdf
BuildRequires:  fontpackages-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gperf
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  ninja-build
# /oreon:deps
%description
Fontconfig is designed to locate fonts within the
system and select them according to requirements specified by 
applications.

%package	devel
Summary:	Font configuration and customization library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	freetype-devel >= %{freetype_version}
Requires:	pkgconfig
Requires:	gettext
%description	devel
The fontconfig-devel package includes the header files,
and developer docs for the fontconfig package.

Install fontconfig-devel if you want to develop programs which 
will use fontconfig.

%package	devel-doc
Summary:	Development Documentation files for fontconfig library
BuildArch:	noarch
Requires:	%{name}-devel = %{version}-%{release}
%description	devel-doc
The fontconfig-devel-doc package contains the documentation files
which is useful for developing applications that uses fontconfig.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# To reduce a maintenance cost of fontconfig-lower-nonlatin-conf.patch
mv conf.d/65-nonlatin.conf conf.d/69-nonlatin.conf

%build

%meson -Ddoc=disabled -Dcache-build=disabled -Dxml-backend=libxml2 \
       -Dadditional-fonts-dirs=/usr/share/X11/fonts/Type1,/usr/share/X11/fonts/TTF,/usr/local/share/fonts \
       -Dcache-dir=/usr/lib/fontconfig/cache \
       --default-library=shared
%meson_build
%install
%meson_install
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_fontconfig_templatedir}/25-unhint-nonlatin.conf $RPM_BUILD_ROOT%{_fontconfig_confdir}/
rm $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/10-sub-pixel-*.conf
rm $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/70-*bitmaps*.conf
install -d $RPM_BUILD_ROOT%{_mandir}/man1
shopt -s nullglob
for f in doc/*.1; do
  install -p -m 0644 "$f" $RPM_BUILD_ROOT%{_mandir}/man1
done
for f in doc/*.txt doc/*.pdf doc/*.html; do
  install -p -m 0644 "$f" .
done
shopt -u nullglob
if [ -f doc/fontconfig-user.sgml ]; then
  touch -r doc/fontconfig-user.sgml fontconfig-user.txt
  touch -r doc/fontconfig-user.sgml fontconfig-user.html
fi
if [ -f doc/fontconfig-devel.sgml ]; then
  touch -r doc/fontconfig-devel.sgml fontconfig-devel.txt
  touch -r doc/fontconfig-devel.sgml fontconfig-devel.html
fi
mv $RPM_BUILD_ROOT%{_bindir}/fc-cache $RPM_BUILD_ROOT%{_bindir}/fc-cache-%{__isa_bits}
echo ".so man1/fc-cache.1" > $RPM_BUILD_ROOT%{_mandir}/man1/fc-cache-%{__isa_bits}.1
install -p -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/fc-cache
%find_lang %{name}
%find_lang %{name}-conf
cat %{name}-conf.lang >> %{name}.lang
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%post

umask 0022
mkdir -p /usr/lib/fontconfig/cache
[[ -d %{_localstatedir}/cache/fontconfig ]] && rm -rf %{_localstatedir}/cache/fontconfig/* 2> /dev/null || :
if [ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache --version 2>&1 | grep -q %{version} ; then
  HOME=/root /usr/bin/fc-cache -f
fi
%transfiletriggerin -- /usr/share/fonts /usr/share/X11/fonts/Type1 /usr/share/X11/fonts/TTF /usr/local/share/fonts
HOME=/root /usr/bin/fc-cache -s
%transfiletriggerpostun -- /usr/share/fonts /usr/share/X11/fonts/Type1 /usr/share/X11/fonts/TTF /usr/local/share/fonts
HOME=/root /usr/bin/fc-cache -s
%posttrans

if [ -e %{_sysconfdir}/xml/catalog ]; then
  %{_bindir}/xmlcatalog --noout --add system \
                        "urn:fontconfig:fonts.dtd" \
                        "file://%{_datadir}/xml/fontconfig/fonts.dtd" \
                        %{_sysconfdir}/xml/catalog
fi
%postun

if [ $1 == 0 ] && [ -e %{_sysconfdir}/xml/catalog ]; then
  %{_bindir}/xmlcatalog --noout --del "urn:fontconfig:fonts.dtd" %{_sysconfdir}/xml/catalog
fi
%files -f %{oreon_filedir}/main.list
%files -n fontconfig-devel -f %{oreon_filedir}/fontconfig-devel.list
%files -n fontconfig-devel-doc -f %{oreon_filedir}/fontconfig-devel-doc.list

%changelog

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17.0-7
- %%install use nullglob for doc man globs when meson -Ddoc=disabled leaves no doc/*.1
- Source0 from GitLab tag archive (freedesktop release/fontconfig-2.17.0.tar.xz 404)
- Replace deprecated PreReq with Requires(pre) for freetype

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17.0-5
- Source from www.freedesktop.org/software/fontconfig/release (fontconfig.org path 404)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17.0-4
- Prepare for Oreon 11 (RP1)
