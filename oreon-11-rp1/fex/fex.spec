%global source0_hash b023711ddab9e656c077921c94d4346e21ab60d8c6d80b00191f3d581f4dfd7c

Name:    fex
Version: 2.0.0
Release: 25%{?dist}
Summary: Field split/extraction like cut/awk
License: Apache-2.0
URL:     http://semicomplete.com/projects/fex/
Source0: https://github.com/jordansissel/%{name}/archive/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: perl(Pod::Man)
BuildRequires: make

%description
Fex is a powerful field extraction tool. Fex provides a very concise language
for tokenizing strings and extracting fields.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# snprintf has a license incompatible with Fedora
# It is only used on Solaris so just delete the directory to avoid confusion or
# problems with licensing.
rm -rf snprintf_2.2

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"
make %{?_smp_mflags} CFLAGS="%{optflags}" fex.1

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}  PREFIX=%{_prefix}

%files
%doc LICENSE README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
%autochangelog
