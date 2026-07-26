%global source0_hash none

%global pkg irsim-mode
%global pkgname Emacs-irsim-mode

%if %($(pkg-config emacs) ; echo $?)
%global emacs_version 21.1
%global emacs_lispdir %{_datadir}/emacs/site-lisp
%global emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d
%else
%global emacs_version %(pkg-config emacs --modversion)
%global emacs_lispdir %(pkg-config emacs --variable sitepkglispdir)
%global emacs_startdir %(pkg-config emacs --variable sitestartdir)
%endif

Name:		emacs-%{pkg}
Version:	0.1
Release:	35%{?dist}
Summary:	Irsim mode for emacs

License:	MIT
URL:		http://code.google.com/p/irsim-mode/
Source0:	http://irsim-mode.googlecode.com/files/irsim-mode.el
Source1:	%{pkg}-init.el

BuildArch:	noarch
BuildRequires:	emacs emacs-el
Requires:	emacs >= %{emacs_version}
		
Obsoletes:	%{name}-el < 0.1-31
Provides:	%{name}-el = %{version}-%{release}

%description
IRSIM is a switch-level simulator for digital logic circuits.
This is an Emacs mode for editing IRSIM netlists. It provides
syntax highlighting and an extremely pleasant method of indentation.

%prep
%{__rm} -rf %{_builddir}/%{name}-%{version}
%{__mkdir} -p %{_builddir}/%{name}-%{version}
cp -p %{SOURCE0} %{_builddir}/%{name}-%{version}
cp -p %{SOURCE1} %{_builddir}/%{name}-%{version}

%build
cd %{name}-%{version}
emacs -batch -f batch-byte-compile %{pkg}.el

%install
%{__rm} -rf %{buildroot}
cd %{name}-%{version}
%{__install} -pm 755 -d %{buildroot}%{emacs_lispdir}/irsim-mode/
%{__install} -pm 755 -d %{buildroot}%{emacs_startdir}	
%{__install} -pm 644 %{pkg}.* %{buildroot}%{emacs_lispdir}/%{pkg}
%{__install} -pm 644 %{SOURCE1} %{buildroot}%{emacs_startdir}

%files
%{emacs_lispdir}/%{pkg}/*.el
%{emacs_lispdir}/%{pkg}/*.elc
%{emacs_startdir}/%{pkg}-init.el
%dir %{emacs_lispdir}/%{pkg}
%dir %{emacs_startdir}

%changelog
%autochangelog
