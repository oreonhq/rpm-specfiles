%global source0_hash 3959bce8ffeb1924323f6fa1fa34ac53d18ad7785a8f6b27e7ff878e6d11f817

%global debug_package   %nil

# this enforces us to create non-noarch package
%global native_dir      %_libdir/mozilla/native-messaging-hosts

%global __brp_python_bytecompile :

Name:           textern
Version:        0.8
Release:        8%{?dist}
Summary:        Firefox add-on for editing text in your favorite external editor

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/jlebon/textern

Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         textern-0.7-system-inotify-simple.patch

Requires:       mozilla-filesystem
Requires:       python3-inotify_simple

BuildRequires:  make
BuildRequires:  python3-devel

%description
Textern is a Firefox add-on that allows you to edit text areas in web pages
using an external editor.  It is similar in functionality to the popular
It's All Text! add-on, though makes use of the WebExtension API and is thus
fully compatible with multiprocessing and supported beyond Firefox 57.

This is not a self-standing Firefox add-on, it's only the "native" application
used by Add-on named "textern".  Please install the Add-on manually.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build

%install
make native-install \
    PREFIX=/usr \
    MOZILLA_NATIVE=%native_dir \
    DESTDIR=%buildroot

%files
%license LICENSE
%doc README.md
%dir %native_dir
%native_dir/textern.json
%dir %_libexecdir/textern
%_libexecdir/textern/textern.py

%changelog
%autochangelog
