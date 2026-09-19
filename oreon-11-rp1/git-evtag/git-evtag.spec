%global source0_hash ce8b37638f1fb92f347200b419da074be8515be9b55791116e9cab22d9cd5a67

Summary: Strong GPG verification of git tags
Name: git-evtag
Version: 2022.1
Release: %autorelease

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
#VCS: https://github.com/cgwalters/git-evtag
URL: https://github.com/cgwalters/git-evtag
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc

BuildRequires: meson
BuildRequires: /usr/bin/xsltproc
BuildRequires: docbook-style-xsl
BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(gio-2.0)

Requires: git
Requires: gnupg2

%description
git-evtag wraps "git tag" functionality, adding stronger checksums
that cover the complete content.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/git-evtag.1*

%changelog
%autochangelog
