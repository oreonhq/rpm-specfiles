# ifdef'd in source code but runtime dep will be made for FT_Done_MM_Var symbol in freetype-2.9.1
# so update the build deps as well to keep deps consistency between runtime and build time.
%global freetype_version 2.9.1

Summary:	Font configuration and customization library
Name:		fontconfig
Version:	2.17.0
Release:	7%{?dist}
# src/ftglue.[ch] is in Public Domain
# src/fccache.c contains Public Domain code
## https://gitlab.com/fedora/legal/fedora-license-data/-/issues/177
# fc-case/CaseFolding.txt is in the UCD
# otherwise MIT
License:	HPND AND LicenseRef-Fedora-Public-Domain AND Unicode-DFS-2016
# Official release tarball on freedesktop.org is missing for some tags; GitLab tag archive matches upstream.
Source:		https://gitlab.freedesktop.org/fontconfig/fontconfig/-/archive/%{version}/fontconfig-%{version}.tar.bz2
URL:		http://fontconfig.org
Source1:	25-no-bitmap-fedora.conf
Source2:	fc-cache

# https://bugzilla.redhat.com/show_bug.cgi?id=140335
Patch0:		%{name}-sleep-less.patch
Patch4:		%{name}-drop-lang-from-pkgkit-format.patch
Patch5:		%{name}-disable-network-required-test.patch
Patch6:		%{name}-lower-nonlatin-conf.patch
Patch7:		%{name}-fix-crash.patch
# oreon url source checksums begin
%global source0_sha256 486c53e63c07cefd56ccd1234a665bc45fa2f37072c189ccb06373b97c7d73c2
%global source0_file fontconfig-2.17.0.tar.bz2
# oreon url source checksums end

BuildRequires:	libxml2-devel
BuildRequires:	freetype-devel >= %{freetype_version}
BuildRequires:	fontpackages-devel
BuildRequires:	gettext
BuildRequires:	gperf
BuildRequires:  docbook-utils docbook-utils-pdf
BuildRequires:  meson ninja-build gcc

Requires:	fonts-filesystem freetype
# Register DTD system-wide to make validation work by default
# (used by fonts-rpm-macros)
Requires(pre):    xml-common
Requires(postun): xml-common
Requires(pre):	freetype >= 2.9.1-6
Requires(post):	grep coreutils
Requires:	font(:lang=en)
Suggests:	font(notosans)

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/fontconfig-2.17.0.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "486c53e63c07cefd56ccd1234a665bc45fa2f37072c189ccb06373b97c7d73c2" || { echo "oreon: Source0 SHA256 mismatch for fontconfig-2.17.0.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
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

# Use implied value to allow the use of conditional conf
rm $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/10-sub-pixel-*.conf

# Do not enable bitmap-related conf
rm $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/70-*bitmaps*.conf

# Install extra docs when present (-Ddoc=disabled means no prebuilt doc/*.[135] in tree)
install -d $RPM_BUILD_ROOT%{_mandir}/man1
shopt -s nullglob
for f in doc/*.1; do
  install -p -m 0644 "$f" $RPM_BUILD_ROOT%{_mandir}/man1
done
for f in doc/*.txt doc/*.pdf doc/*.html; do
  install -p -m 0644 "$f" .
done
shopt -u nullglob

# adjust the timestamp to avoid conflicts for multilib
if [ -f doc/fontconfig-user.sgml ]; then
  touch -r doc/fontconfig-user.sgml fontconfig-user.txt
  touch -r doc/fontconfig-user.sgml fontconfig-user.html
fi
if [ -f doc/fontconfig-devel.sgml ]; then
  touch -r doc/fontconfig-devel.sgml fontconfig-devel.txt
  touch -r doc/fontconfig-devel.sgml fontconfig-devel.html
fi

# rename fc-cache binary
mv $RPM_BUILD_ROOT%{_bindir}/fc-cache $RPM_BUILD_ROOT%{_bindir}/fc-cache-%{__isa_bits}

# create link to man page
echo ".so man1/fc-cache.1" > $RPM_BUILD_ROOT%{_mandir}/man1/fc-cache-%{__isa_bits}.1

install -p -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/fc-cache

%find_lang %{name}
%find_lang %{name}-conf
cat %{name}-conf.lang >> %{name}.lang

%check
%meson_test

%post
umask 0022

mkdir -p /usr/lib/fontconfig/cache

[[ -d %{_localstatedir}/cache/fontconfig ]] && rm -rf %{_localstatedir}/cache/fontconfig/* 2> /dev/null || :

# Force regeneration of all fontconfig cache files
# The check for existance is needed on dual-arch installs (the second
#  copy of fontconfig might install the binary instead of the first)
# The HOME setting is to avoid problems if HOME hasn't been reset
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

%files -f %{name}.lang
%doc README.md AUTHORS
%doc fontconfig-user.txt fontconfig-user.html
%doc %{_fontconfig_confdir}/README
%license COPYING
%{_libdir}/libfontconfig.so.*
%{_bindir}/fc-cache*
%{_bindir}/fc-cat
%{_bindir}/fc-conflist
%{_bindir}/fc-list
%{_bindir}/fc-match
%{_bindir}/fc-pattern
%{_bindir}/fc-query
%{_bindir}/fc-scan
%{_bindir}/fc-validate
%{_fontconfig_templatedir}/*.conf
%{_datadir}/xml/fontconfig
# fonts.conf is not supposed to be modified.
# If you want to do so, you should use local.conf instead.
%config %{_fontconfig_masterdir}/fonts.conf
%config(noreplace) %{_fontconfig_confdir}/*.conf
%dir /usr/lib/fontconfig
%dir /usr/lib/fontconfig/cache
%{_mandir}/man1/*

%files devel
%{_libdir}/libfontconfig.so
%{_libdir}/pkgconfig/*
%{_includedir}/fontconfig
%{_datadir}/gettext/its/fontconfig.its
%{_datadir}/gettext/its/fontconfig.loc

%files devel-doc
%doc fontconfig-devel.txt fontconfig-devel.html

%changelog
* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17.0-7
- %%install use nullglob for doc man globs when meson -Ddoc=disabled leaves no doc/*.1
- Source0 from GitLab tag archive (freedesktop release/fontconfig-2.17.0.tar.xz 404)
- Replace deprecated PreReq with Requires(pre) for freetype

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17.0-5
- Source from www.freedesktop.org/software/fontconfig/release (fontconfig.org path 404)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17.0-4
- Prepare for Oreon 11 (RP1)
