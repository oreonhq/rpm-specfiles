%global source0_hash c24a9c24337e556250f72252283f19d97d43cbe6cea61d95822a82f27fc6002e

# This is the date of the latest upstream git commit.
%global verdate 20150501

Name:           avgtime
Version:        0.5.1
Release:        0.51.git%{verdate}%{?dist}
Summary:        Time a command and print average, standard deviation

# Automatically converted from old format: Boost - review is highly recommended.
License:        BSL-1.0
URL:            https://github.com/jmcabo/avgtime

# There are no upstream source tarballs.  The source tarball
# here was constructed as follows:
#
#   git clone https://github.com/jmcabo/avgtime.git
#   cd avgtime
#   d=YYYYMMDD  # date of latest upstream git commit
#   git archive -o /tmp/avgtime-$d.tar.gz --prefix=avgtime-$d/ HEAD
#
Source0:        avgtime-%{verdate}.tar.gz

ExclusiveArch:  %{ldc_arches}

BuildRequires:  ldc

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

%files
%license LICENSE_1_0.txt
%doc README.md
%{_bindir}/avgtime

%changelog
%autochangelog
