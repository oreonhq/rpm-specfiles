%global source0_hash 58cda97d444405918f1e15b698a5cb2a72dd152a1d93e3ac23e001634690d6cf

Summary:	Display memory information graphically
Name:		freecolor
Version:	0.9.3
Release:	25%{?dist}

License:	MIT
URL:		http://www.rkeene.org/oss/freecolor/
Source0:	http://www.rkeene.org/files/oss/freecolor/freecolor-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make

%description
Freecolor displays the total amount of free and used physical and swap
memory in the system as a colored bargraph on the command line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
install -Dpm 0755 free %{buildroot}/%{_bindir}/freecolor
install -Dpm 0644 freecolor.1 %{buildroot}/%{_mandir}/man1/freecolor.1

%files
%license COPYING
%doc README
%{_bindir}/freecolor
%{_mandir}/man1/*.1*

%changelog
%autochangelog
