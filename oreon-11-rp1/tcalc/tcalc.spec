%global source0_hash 09ee253cfb11727aa0c8628d3c4190ce2955eea3f8ebf0242253473673e38596

Name:           tcalc
Version:        2.1
Release:        25%{?dist}
Summary:        The terminal calculator

License:        GPL-3.0-or-later
URL:            http://sites.google.com/site/mohammedisam2000/home/projects
Source:         %{url}/%{name}-%{version}.tar.gz

Patch0:         0000-fix-compilation-errors.patch

BuildRequires:  gcc
BuildRequires:  make

%description
The terminal calculator is a small and helpful program to help users of the
GNU/Linux terminal do calculations simply and quickly. The formula to be
calculated can be fed to tcalc through the command line. Alternatively, tcalc
can be run with no formula and then the free mode is started, in which the 
calculator will wait for user input, do the necessary calculations and print 
out the result, and the cycle will repeat until the user enters 'q' or 'quit'.
Support for reading formulas from text files is under way.

The calculator works with the decimal, hexadecimal, octal, and binary number
systems. It automatically identifies hex numbers if entered with a preceding 
"0x" or "0X", octal by preceding the number with a zero, binaries by 
preceding the number with 'b' and decimals by absence of all of the above. 
Alternatively, the user can indicate the type of input by setting the 'format' 
argument.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

# Install info page
install -m 0644 -p -D info/tcalc.info* %{buildroot}%{_infodir}/tcalc.info

# Reshuffle docs and examples
rm -r %{buildroot}%{_docdir}/%{name}
mkdir examples
mv test test2 examples/

%files
%license COPYING
%doc README AUTHORS ChangeLog examples/
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_infodir}/%{name}.info*

%changelog
%autochangelog
