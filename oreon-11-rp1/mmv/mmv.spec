%global source0_hash 2bbba14c099b512b4a7e9effacec53caa06998069d108a5669ff424ffc879d03

Name:		mmv
Version:	2.10
Release:	3%{?dist}
Summary:	Move/copy/link multiple files

License:	GPL-3.0-or-later
URL:		https://github.com/rrthomas/mmv
Source0:	https://github.com/rrthomas/mmv/releases/download/v%{version}/mmv-%{version}.tar.gz
BuildRequires:	make gcc gc-devel

%description
This is mmv, a program to move/copy/append/link multiple files
according to a set of wildcard patterns. This multiple action is
performed safely, i.e. without any unexpected deletion of files due to
collisions of target names with existing filenames or with other
target names. Furthermore, before doing anything, mmv attempts to
detect any errors that would result from the entire set of actions
specified and gives the user the choice of either aborting before
beginning, or proceeding by avoiding the offending parts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%make_build

%install
%make_install
ln -s mmv.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/mcp.1.gz
ln -s mmv.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/mln.1.gz
ln -s mmv.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/mad.1.gz

%check
make check

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/mmv
%{_bindir}/mcp
%{_bindir}/mln
%{_bindir}/mad
%{_mandir}/man1/*.1*

%changelog
%autochangelog
