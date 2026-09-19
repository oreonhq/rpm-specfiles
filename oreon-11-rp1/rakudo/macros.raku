# Raku-specific RPM build macros for Raku modules.

%__raku                 /usr/bin/rakudo
%rakudo_rpm_version     %{version}
%raku_vendor_dir        /usr/share/perl6/vendor
%raku_site_dir          /usr/share/perl6/site
%raku_mod_inst          /usr/bin/raku-install-dist

%__perl6                %{__raku}
%perl6_vendor_dir       %{raku_vendor_dir}
%perl6_site_dir         %{raku_site_dir}
%perl6_mod_inst         %{raku_mod_inst}
