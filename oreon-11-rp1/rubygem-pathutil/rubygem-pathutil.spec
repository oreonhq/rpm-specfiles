%global source0_hash c7fe1ba37ec11ae35fa5c7fb9b5ba4633ca3ca0cf68b352705a3c96d3a278438

%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global gem_name pathutil

Name:		rubygem-%{gem_name}
Version:	0.14.0
Release:	20%{?dist}
Summary:	Faster pure Ruby implementation of Pathname with extra bits

License:	MIT
URL:		https://github.com/envygeeks/%{gem_name}
Source0:	https://rubygems.org/downloads/%{gem_name}-%{version}.gem
Source1:	https://raw.githubusercontent.com/envygeeks/pathutil/master/README.md#/%{gem_name}-README.md

BuildArch:	noarch
BuildRequires:	rubygems-devel

%description
Pathutil tries to be a faster pure Ruby implementation of Pathname.
It arose out of a need to fix basic problems with Pathname, such as
susceptibility to join overrides, need for automatic encoding, and
normalization (for stuff like Jekyll) and the ability to do other
safe-style operations in an encapsulated format, like copying files
and folders with symbolic links but only if they originate from the
given root.

%package doc
Summary:	Documentation files for %{name}

%description doc
This package contains the documentation files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{__rm} -rf %{gem_name}-%{version}
%{_bindir}/gem unpack %{SOURCE0}
%setup -DTqn %{gem_name}-%{version}
%{_bindir}/gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
%{_bindir}/gem build %{gem_name}.gemspec
%gem_install

%install
%{__mkdir} -p %{buildroot}%{gem_dir}
%{__cp} -a ./%{gem_dir}/* %{buildroot}%{gem_dir}
%{__rm} -f %{buildroot}%{gem_instdir}/{LICENSE,Rakefile}
%{__install} -pm0644 %{SOURCE1} ./README.markdown

%files
%exclude %{gem_cache}
%license LICENSE
%doc README.markdown
%{gem_instdir}
%{gem_spec}

%files doc
%doc %{_pkgdocdir}
%doc %{gem_docdir}

%changelog
%autochangelog
