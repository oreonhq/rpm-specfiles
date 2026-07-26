%global source0_hash dab03dd30ad5a58e578c5581241a6e87e184a18eb2c3b2e0fffa8a9cf105c97b

Name:           pwgen
Version:        2.08
Release:        18%{?dist}
Summary:        Automatic password generation

License:        GPL-1.0-or-later
URL:            http://sf.net/projects/pwgen
Source0:        http://download.sf.net/pwgen/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc

%description
pwgen generates random, meaningless but pronounceable passwords. These
passwords contain either only lowercase letters, or upper and lower case, or
upper case, lower case and numeric digits. Upper case letters and numeric
digits are placed in a way that eases memorizing the password.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%doc debian/changelog
%license debian/copyright
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
