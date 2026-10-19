%global source0_hash f96f73c54521c53f14dc164d5a3920c9ca21a0e5f8e9613f43812a98af3e22af
Name:           colordiff
Version:        1.0.22
Release:        1%{?dist}
Summary:        Color terminal highlighter for diff files
License:        GPL-2.0-or-later
URL:            http://www.colordiff.org/
Source0:        http://www.colordiff.org/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       diffutils
Requires:       less
Recommends:     bzip2
Recommends:     gzip
Recommends:     xz
Suggests:       curl
Provides:       cdiff
# oreon:deps
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
Colordiff is a wrapper for diff and produces the same output but with
pretty syntax highlighting.  Color schemes can be customized.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
%make_install INSTALL_DIR=%{_bindir} \
    ETC_DIR=%{_sysconfdir} MAN_DIR=%{_mandir}/man1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
