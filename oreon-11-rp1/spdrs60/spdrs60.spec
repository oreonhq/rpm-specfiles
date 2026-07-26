%global source0_hash f141f6e88f35e7e429542950171db17e1f61ec660baaf1f50dae45e837eef08c

Summary:	SRCP based locking table for digital model railroads
Name:		spdrs60
Version:	0.6.5
Release:	9%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://spdrs60.sourceforge.net/
Source:		http://sourceforge.net/projects/spdrs60/files/spdrs60/%{version}/spdrs60-%{version}.tar.bz2

BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-style-dsssl
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qttools-devel
BuildRequires:	openjade

%description
Graphical program to comfortably control a digital model railroad.
Visual appearance and usage comply to the SpDr of the German national
railroad company. SpDrS60 needs a Simple Railroad Command Protocol
(SRCP) server (e.g. erddcd or srcpd) as a link to the physical layout
of the model.

%package	doc
Summary:	Documentation for %{name}
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
for file in ./AUTHORS ./NEWS; do
	iconv -f latin1 -t utf8 < $file > $file.new
	mv -f $file.new $file
done

%build
%configure
%make_build

%install
%make_install
%find_lang %{name} --with-man --all-name

cp -p spdrs60.redhat.desktop spdrs60.desktop
desktop-file-install \
	--remove-key='Encoding' \
	--set-key='Terminal' \
	--set-value='false' \
	--remove-category='Application' \
	--delete-original \
	--dir='%{buildroot}%{_datadir}/applications' \
	spdrs60.desktop

%files -f %{name}.lang
%doc AUTHORS README TODO NEWS ChangeLog spdrs60.lsm
%license COPYING
%{_bindir}/%{name}
%{_bindir}/centralclock
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*
%{_mandir}/man1/*.1*

%files doc
%docdir %{_docdir}/%{name}/html
%{_docdir}/%{name}/html

%changelog
%autochangelog
