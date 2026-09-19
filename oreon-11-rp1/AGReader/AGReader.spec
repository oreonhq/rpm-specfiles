%global source0_hash a8ddd38ac43d9b6f156334a471a66fa93bb83695ef3a99ce62eb8ea3f44e5c08

Name:           AGReader
Version:        1.2
Release:        42%{?dist}
Summary:        Console reader for viewing AmigaGuide files
License:        GPL-1.0-or-later
URL:            http://main.aminet.net/misc/unix/
Source0:        http://main.aminet.net/misc/unix/%{name}.tar.bz2
Source1:        agr.1
BuildRequires:  gcc
BuildRequires: make

%description
A viewer for the UNIX console which can read and display AmigaGuide files. It
supports all of the v39 AmigaGuide specification possible and supports a large
subset of the v40 specifications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}

%build
%make_build -C Sources CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m0644 %{SOURCE1} %{buildroot}%{_mandir}/man1
install -m0755 Sources/agr %{buildroot}%{_bindir}

%files
%{_bindir}/agr
%{_mandir}/man1/agr.1.gz
%doc Docs/agr.guide Docs/test.guide Docs/agr.html README

%changelog
%autochangelog
