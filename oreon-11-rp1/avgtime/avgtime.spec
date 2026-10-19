%global source0_hash c24a9c24337e556250f72252283f19d97d43cbe6cea61d95822a82f27fc6002e
%global verdate 20150501
Name:           avgtime
Version:        0.5.1
Release:        1%{?dist}
Summary:        Time a command and print average, standard deviation
License:        BSL-1.0
URL:            https://github.com/jmcabo/avgtime
Source0:        %{name}-%{verdate}.tar.gz
ExclusiveArch:  %{ldc_arches}
# oreon:deps
BuildRequires:  ldc
# /oreon:deps
%description
'avgtime' works like the Linux 'time' command, except it runs the
command repeatedly and displays statistics:

- median
- average
- standard deviation
- 95% and 99% confidence intervals

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n avgtime-%{verdate}

%build

ldc2 %{_d_optflags} avgtime.d
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -a avgtime $RPM_BUILD_ROOT%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
