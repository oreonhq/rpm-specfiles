%global source0_hash fe55fd6fb0bdadc2c7c6dff05cb4651f379661b3fd1c6ae302920f51e5a72050

Name:           xblast-data
Version:        2.10.0
Release:        34%{?dist}
Summary:        Data files for the game xblast
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://xblast.sourceforge.net
Source0:        http://downloads.sourceforge.net/xblast/xblast-complete-sounds-%{version}.tar.gz
BuildRequires:  convmv
BuildArch:      noarch
Requires:       xblast-engine >= %{version}

%description
This package contains the data files for XBlast, a multiplayer game where the
"purpose" is to Blast the other players of the gamefield by laying bombs close
to them. While at the same time you must avoid being blown up yourself.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n xblast-%{version}
convmv --notest -f ISO_8859-1 -t UTF-8 level/reconstruct*
# stop these from getting installed
rm `find -name Imakefile`

%build
# nothing to build data only

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xblast
cp -a image level sounds $RPM_BUILD_ROOT%{_datadir}/xblast

%files
%doc AUTHORS ChangeLog COPYING README NEWS
%{_datadir}/xblast

%changelog
%autochangelog
