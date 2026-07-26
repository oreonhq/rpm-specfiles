%global source0_hash 93a9f8b83a19cd61d1f7f306f8ddebea8f5ea11f3a4d236ec843ba50cea58dea

Name:           colordiff
Version:        1.0.22
Release:        1%{?dist}
Summary:        Color terminal highlighter for diff files

License:        GPL-2.0-or-later
URL:            http://www.colordiff.org/
Source0:        http://www.colordiff.org/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  make
Requires:       diffutils
Requires:       less
Recommends:     bzip2
Recommends:     gzip
Recommends:     xz
Suggests:       curl
Provides:       cdiff

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

%files
%license COPYING
%doc BUGS CHANGES colordiffrc colordiffrc-gitdiff colordiffrc-lightbg README
%config(noreplace) %{_sysconfdir}/colordiffrc
%{_bindir}/cdiff
%{_bindir}/colordiff
%{_mandir}/man1/cdiff.1*
%{_mandir}/man1/colordiff.1*

%changelog
%autochangelog
