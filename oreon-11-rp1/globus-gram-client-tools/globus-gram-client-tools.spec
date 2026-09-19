%global source0_hash e632fa5986894c8a74f39ed6a2153bfe445d9550119ebe48273e867f445042bc

Name:		globus-gram-client-tools
%global _name %(tr - _ <<< %{name})
Version:	12.2
Release:	10%{?dist}
Summary:	Grid Community Toolkit - Job Management Tools (globusrun)

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-gram-client-devel >= 12
BuildRequires:	globus-gram-protocol-devel >= 11
BuildRequires:	globus-gass-transfer-devel >= 7
BuildRequires:	globus-gass-server-ez-devel >= 4
BuildRequires:	globus-rsl-devel >= 9
BuildRequires:	globus-gss-assist-devel >= 8

Requires:	globus-common-progs >= 15

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Job Management Tools (globusrun)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

%make_build

%install
%make_install

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%files
%{_bindir}/globus-job-cancel
%{_bindir}/globus-job-clean
%{_bindir}/globus-job-get-output
%{_bindir}/globus-job-get-output-helper
%{_bindir}/globus-job-run
%{_bindir}/globus-job-status
%{_bindir}/globus-job-submit
%{_bindir}/globusrun
%doc %{_mandir}/man1/globus-job-cancel.1*
%doc %{_mandir}/man1/globus-job-clean.1*
%doc %{_mandir}/man1/globus-job-get-output.1*
%doc %{_mandir}/man1/globus-job-get-output-helper.1*
%doc %{_mandir}/man1/globus-job-run.1*
%doc %{_mandir}/man1/globus-job-status.1*
%doc %{_mandir}/man1/globus-job-submit.1*
%doc %{_mandir}/man1/globusrun.1*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%changelog
%autochangelog
