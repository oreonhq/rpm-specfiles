%global source0_hash 3477a0e5568e241c63c9899accbfcdb6aadef2812fcce0173688567b4c7d4025

Name:           httrack
Version:        3.49.2
Release:        %autorelease
Summary:        Website copier and offline browser
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.httrack.com
Source0:        http://mirror.httrack.com/historical/%{name}-%{version}.tar.gz
Patch0: httrack-configure-c99.patch
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires: make
Requires:       hicolor-icon-theme
Requires:       xdg-utils

%description
HTTrack is a free and easy-to-use offline browser utility. It allows the user 
to download a World Wide Web site from the Internet to a local directory, 
building recursively all directories, getting HTML, images, and other files 
from the server to your computer. HTTrack arranges the original site's 
relative link-structure. HTTrack can also update an existing mirrored site, 
and resume interrupted downloads. HTTrack is fully configurable, and has an 
integrated help system.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Do not try to re-run autoconf after patching generated files.
touch -r aclocal.m4 m4/*.m4 configure

# Suppress rpmlint error.
iconv --from-code ISO8859-1 --to-code UTF-8 ./html/contact.html \
  --output contact.utf-8 && mv contact.utf-8 ./html/contact.html

%build
 %{!?_pkgdocdir: %global _pkgdocdir /usr/share/doc/httrack}
%configure  --disable-static \
            --disable-online-unit-tests \
            --htmldir=%{_pkgdocdir}/html \
            --docdir=%{_pkgdocdir}

# Remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
%make_install

# Remove static libraries.
find %{buildroot} -type f -name "*.*a" -delete -print

# Remove unnecessary dynamic libraries from %%{_libdir}/httrack. These come
# from libtest, just a sample project from upstream.
rm -frv %{buildroot}%{_libdir}/%{name}

# Move libtest and templates from %%{_datadir}/httrack into %%{_pkgdocdir}.
mv %{buildroot}%{_datadir}/%{name}/libtest %{buildroot}%{_pkgdocdir}/libtest
mv %{buildroot}%{_datadir}/%{name}/templates %{buildroot}%{_pkgdocdir}/templates

# Now packaged in %%license
rm %{buildroot}%{_pkgdocdir}/html/license.txt

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/WebHTTrack.desktop

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/WebHTTrack-Websites.desktop

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make check -C tests

%pretrans -p <lua>
--[[Script below fixes some crufts introduced in httrack < 3.47.26-1, to
cleanup wrong symlinks in old httrack packages.
In the past it's a shell script, it worked but another problem came in,
as if users are installing a fresh Fedora then they will fail at here.
This is because coreutils is not installed in pretrans stage although
fresh Fedora doesn't contain directory we want to remove.

https://fedoraproject.org/wiki/Packaging:Directory_Replacement
]]
require "os"
require "posix"

local path1 = "%{_datadir}/httrack/html"
local st1 = posix.stat(path1)
if st1 and st1.type == "directory" then
  local status1 = os.rename(path1, path1..".rpmmoved")
  if not status1 then
    local suffix1 = 0
    while not status1 do
      suffix1 = suffix1 + 1
      status1 = os.rename(path1..".rpmmoved", path1..".rpmmoved."..suffix1)
    end
    os.rename(path1, path1..".rpmmoved")
  end
end

local path2 = "%{_pkgdocdir}/html"
local st2 = posix.stat(path2)
if st2 and st2.type == "link" then
  os.remove(path2)
end

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %doc}
%{_pkgdocdir}
%exclude %{_pkgdocdir}/libtest
%license COPYING license.txt
%{_bindir}/htsserver
%{_bindir}/%{name}
%{_bindir}/proxytrack
%{_bindir}/webhttrack
%{_datadir}/applications/*WebHTTrack.desktop
%{_datadir}/applications/*WebHTTrack-Websites.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}*x*.xpm
%{_datadir}/%{name}/
%{_libdir}/libhtsjava.so.*
%{_libdir}/libhttrack.so.*
%{_mandir}/man1/htsserver.1*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/proxytrack.1*
%{_mandir}/man1/webhttrack.1*

%files devel
%{_pkgdocdir}/libtest/
%{_includedir}/%{name}/
%{_libdir}/libhtsjava.so
%{_libdir}/libhttrack.so

%changelog
%autochangelog
