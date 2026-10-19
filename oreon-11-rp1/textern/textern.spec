%global source0_hash 3959bce8ffeb1924323f6fa1fa34ac53d18ad7785a8f6b27e7ff878e6d11f817
%global debug_package   %nil
%global native_dir      %_libdir/mozilla/native-messaging-hosts
%global __brp_python_bytecompile :
Name:           textern
Version:        0.8
Release:        1%{?dist}
Summary:        Firefox add-on for editing text in your favorite external editor
License:        GPL-3.0-or-later
URL:            https://github.com/jlebon/textern
Source0:        https%{__brp_python_bytecompile}//github.com/jlebon/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         textern-0.7-system-inotify-simple.patch
Requires:       mozilla-filesystem
Requires:       python3-inotify_simple
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
Textern is a Firefox add-on that allows you to edit text areas in web pages
using an external editor.  It is similar in functionality to the popular
It's All Text! add-on, though makes use of the WebExtension API and is thus
fully compatible with multiprocessing and supported beyond Firefox 57.

This is not a self-standing Firefox add-on, it's only the "native" application
used by Add-on named "textern".  Please install the Add-on manually.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
make native-install \
    PREFIX=/usr \
    MOZILLA_NATIVE=%native_dir \
    DESTDIR=%buildroot
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
