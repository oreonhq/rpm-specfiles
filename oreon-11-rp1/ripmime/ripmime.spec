%global source0_hash 6d551d6b65b4da6c6b8dfd05be8141026cc760ca1fb8a707b7bf96c199c9f52d

Name:           ripmime
Version:        1.4.1.0
Release:        5%{?dist}
Summary:        Extract attachments out of a MIME encoded email packages

License:        BSD-3-Clause
URL:            http://www.pldaniels.com/ripmime/
Source0:        https://github.com/inflex/RIPmime/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc

%description
ripMIME extract attachments out of a MIME encoded email packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ripMIME-%{version}

%build
%make_build CFLAGS="%{optflags}"

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/ripmime.1*
%doc CHANGELOG CONTRIBUTORS INSTALL TODO README
%license LICENSE

%changelog
%autochangelog
