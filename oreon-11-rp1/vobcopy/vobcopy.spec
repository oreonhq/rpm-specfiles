%global source0_hash f4737efaf5ad4f84b5c94ca82cda04dbb20c59cebc23588e3662e0c2813d6fde

Name:           vobcopy
Version:        1.2.1
Release:        9%{?dist}
Summary:        Utility to copy DVD .vob files to disk

License:        GPL-2.0-or-later
URL:            https://github.com/barak/vobcopy
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Update GPLv2 license text
Patch:          %{url}/pull/19.patch

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  gettext-devel
BuildRequires:  libdvdread-devel

%description
Vobcopy copies DVD .vob files to disk via libdvdread and merges them into
file(s) with the name extracted from the DVD. There is one drawback though:
at the moment vobcopy doesn't deal with multi-angle DVDs. But since these are
rather sparse this shouldn't matter much.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -fiv

# Convert German manpage to UTF-8
# https://github.com/barak/vobcopy/pull/18
iconv -f iso8859-1 -t utf-8 vobcopy.1.de > vobcopy.1.de.conv && \
  mv -f vobcopy.1.de.conv vobcopy.1.de

%build
%configure
%make_build

%install
%make_install

# Remove the docs we include ourselves as %%doc
rm -r %{buildroot}%{_datadir}/doc

%files
%doc Changelog README Release-Notes TODO
%doc alternative_programs.txt
%license COPYING
%{_bindir}/vobcopy
%{_mandir}/man1/vobcopy.1*
%lang(de) %{_mandir}/de/man1/vobcopy.1*

%changelog
%autochangelog
