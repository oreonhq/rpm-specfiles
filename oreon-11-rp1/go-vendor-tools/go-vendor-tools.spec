%global source0_hash 67cf80e00432f85503041fd91a551bcf8f79c2993337ea5012b9c6b7bed418c6

%bcond check 1
%bcond manpages 1
%bcond scancode %{defined fedora}
%bcond scancode_tests %[ %{with scancode} && "%{_arch}" != "i386" ]

%global forgeurl https://gitlab.com/fedora/sigs/go/go-vendor-tools
%define tag v%{version_no_tilde %{quote:%nil}}

Name:           go-vendor-tools
Version:        0.12.0
%forgemeta
Release:        %autorelease
Summary:        Tools for handling Go library vendoring in Fedora

License:        MIT AND BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with check}
BuildRequires:  askalono-cli
BuildRequires:  trivy
%endif

%if %{with manpages}
BuildRequires:  scdoc
%endif

Recommends:     askalono-cli
Recommends:     go-vendor-tools+scancode
Recommends:     go-vendor-tools+all

%global common_description %{expand:
go-vendor-tools provides tools and macros for handling Go library vendoring in
Fedora.}

%description %common_description

%package doc
Summary:        Documentation for go-vendor-tools
Enhances:       go-vendor-tools

%description doc %common_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 %{forgesetupargs}

%generate_buildrequires
%pyproject_buildrequires -x all%{?with_check:,test}%{?with_scancode_tests:,scancode}

%build
%pyproject_wheel
%if %{with manpages}
./doc/man/mkman.sh
%endif

mkdir -p bash_completions fish_completions zsh_completions
for bin in go_vendor_archive go_vendor_license gocheck2; do
    register-python-argcomplete --shell bash "${bin}" > "bash_completions/${bin}"
    register-python-argcomplete --shell fish "${bin}" > "fish_completions/${bin}.fish"
    if ! (register-python-argcomplete --shell zsh "${bin}" > "zsh_completions/_${bin}"); then
        echo "#compdef ${bin}" > "zsh_completions/_${bin}"
        echo -e "autoload -Uz bashcompinit\nbashcompinit" >> "zsh_completions/_${bin}"
        cat "bash_completions/${bin}" >> "zsh_completions/_${bin}"
    fi
done

%install
%pyproject_install
%pyproject_save_files go_vendor_tools -l

install -Dpm 0644 rpm/macros.go_vendor_tools -t %{buildroot}%{_rpmmacrodir}
install -Dpm 0644 rpm/macros.gocheck2 -t %{buildroot}%{_rpmmacrodir}

mkdir -p %{buildroot}%{_docdir}/go-vendor-tools-doc
cp -rL doc/* %{buildroot}%{_docdir}/go-vendor-tools-doc

%if %{with manpages}
install -Dpm 0644 doc/man/*.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 0644 doc/man/*.5 -t %{buildroot}%{_mandir}/man5/
%endif

install -Dpm 0644 bash_completions/* -t %{buildroot}%{bash_completions_dir}/
install -Dpm 0644 fish_completions/* -t %{buildroot}%{fish_completions_dir}/
install -Dpm 0644 zsh_completions/* -t %{buildroot}%{zsh_completions_dir}/

%if %{with check}
%check
%if %{defined rhel} && %{undefined epel}
export GVTT_FORCE_LICENSE_CHECK_ENABLE=1
%endif
export MACRO_DIR=%{buildroot}%{_rpmmacrodir}
%pytest
%endif

%files -f %{pyproject_files}
%doc *.md
%{_bindir}/gocheck2
%{_bindir}/go_vendor*
%{bash_completions_dir}/go*
%{fish_completions_dir}/go*.fish
%{zsh_completions_dir}/_go*
%{_rpmmacrodir}/macros.gocheck2
%{_rpmmacrodir}/macros.go_vendor_tools
%if %{with manpages}
%{_mandir}/man1/go*.1*
%{_mandir}/man5/go*.5*
%endif

%files doc
%doc %{_docdir}/go-vendor-tools-doc/

%pyproject_extras_subpkg -n go-vendor-tools all %{?with_scancode:scancode}

%changelog
%autochangelog
