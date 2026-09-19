%global source0_hash 271f4b96daece842f1238b191ce9375f7bd997cdf095717b28361536b9d2893d

%global commit d203a4d2bfb32a7a414abc0d4321a6672c428de6
%global date 20210623

%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:     x2gowswrapper
Version:  0.0.0.1
Release:  0.9%{?dist}
Summary:  Helper utility for X2Go HTML5 client
License:  GPL-2.0-or-later
URL:      http://www.x2go.org
# git clone git://code.x2go.org/x2gowswrapper
# cd x2gowswrapper
# git archive --prefix=x2gowswrapper-0.0.0.1-20210623gitd203a4d/ d203a4d2bfb32a7a414abc0d4321a6672c428de6 | gzip >../x2gowswrapper-0.0.0.1-20210623gitd203a4d.tar.gz
Source0:        %{name}/%{name}-%{version}-%{date}git%{shortcommit}.tar.gz

BuildRequires: gcc
BuildRequires: qt5-qtbase-devel

%description
The helper utility x2gowswrapper provides server-side facilities necessary
to support the X2Go HTML5 client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}-%{date}git%{shortcommit}

%build
%qmake_qt5
%make_build

%install
install -D -p --mode=755 x2gowswrapper %{buildroot}%{_sbindir}/x2gowswrapper
install -D -p --mode=644 man/man1/x2gowswrapper.1 %{buildroot}%{_mandir}/man1/x2gowswrapper.1

%files
%license COPYING
%{_sbindir}/x2gowswrapper
%{_mandir}/man1/x2gowswrapper.1*

%changelog
%autochangelog
