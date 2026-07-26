%global source0_hash e7e94ce068878cdb8041602dc41f03e6271835df0b125066cb6fed8c367dfee4

Name:           rpmrebuild
Version:        2.21
Release:        2%{?dist}
Summary:        A tool to build rpm file from rpm database
License:        GPL-2.0-or-later
URL:            http://rpmrebuild.sourceforge.net

Source0:        http://downloads.sourceforge.net/rpmrebuild/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
Requires:       rpm >= 4.0, rpm-build, coreutils, util-linux

%description
A tool to build an RPM file from a package that has already been installed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c 

%build
%make_build

%install
%make_install

%files
%doc AUTHORS Changelog LISEZ.MOI News README Todo rpmrebuild.lsm Version
%license COPYING COPYRIGHT
%{_bindir}/rpmrebuild
%{_prefix}/lib/rpmrebuild
%{_mandir}{,/*}/man1/compat_digest.plug.1rrp*
%{_mandir}{,/*}/man1/demo.plug.1rrp*
%{_mandir}{,/*}/man1/demofiles.plug.1rrp*
%{_mandir}{,/*}/man1/empty_section.plug.1rrp*
%{_mandir}{,/*}/man1/exclude_file.plug.1rrp*
%{_mandir}{,/*}/man1/file2pacDep.plug.1rrp*
%{_mandir}{,/*}/man1/nodoc.plug.1rrp*
%{_mandir}{,/*}/man1/replacefile.plug.1rrp*
%{_mandir}{,/*}/man1/rpmrebuild.1*
%{_mandir}{,/*}/man1/rpmrebuild_plugins.1*
%{_mandir}{,/*}/man1/set_tag.plug.1rrp*
%{_mandir}{,/*}/man1/un_prelink.plug.1rrp*
%{_mandir}{,/*}/man1/uniq.plug.1rrp*
%{_mandir}{,/*}/man1/unset_tag.plug.1rrp*

%changelog
%autochangelog
