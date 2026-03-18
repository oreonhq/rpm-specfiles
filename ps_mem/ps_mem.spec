
Name:           ps_mem
Version:        3.14
Release:        11%{?dist}
Summary:        Memory profiling tool
License:        LGPL-2.1-only
URL:            https://github.com/pixelb/ps_mem

Source0:        https://raw.githubusercontent.com/pixelb/ps_mem/c80287d/ps_mem.py
Source1:        http://www.gnu.org/licenses/lgpl-2.1.txt
Source2:        ps_mem.1

BuildArch:      noarch

BuildRequires:  python3-devel

%description
The ps_mem tool reports how much core memory is used per program
(not per process). In detail it reports:
sum(private RAM for program processes) + sum(Shared RAM for program processes)
The shared RAM is problematic to calculate, and the tool automatically
selects the most accurate method available for the running kernel.


%prep
%setup -q -T -c %{name}-%{version}

cp -p %{SOURCE0} %{name}
cp -p %{SOURCE1} LICENSE
cp -p %{SOURCE2} %{name}.1

# use python3
sed -i "s|/usr/bin/env python|%{__python3}|" %{name}
touch -r %{SOURCE0} %{name}


%install
install -Dpm755 %{name}   %{buildroot}%{_bindir}/%{name}
install -Dpm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%files
%doc LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.14-11
- Prepare for Oreon 11 (RP1)
