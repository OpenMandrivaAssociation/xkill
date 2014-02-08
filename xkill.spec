Name: xkill
Version: 1.0.3
Release: 7
Summary: Kill a client by its X resource
Group: Monitoring
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source11:   %{name}-mini.png
Source12:   %{name}-std.png
Source13:   %{name}-large.png
License: MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xmu) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xkill is a utility for forcing the X server to close connections to clients.
This program is very dangerous, but is useful for aborting programs that have
displayed undesired windows on a user's screen.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -fi
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=XKill
Comment=Kill a client by its X resource
Exec=/usr/bin/xkill
Icon=xkill
Terminal=false
Type=Application
StartupNotify=true
Categories=System;Monitor;
NoDisplay=true
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/xkill.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/xkill.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/xkill.png

%files
%{_bindir}/xkill
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/xkill.png
%{_iconsdir}/xkill.png
%{_liconsdir}/xkill.png


%changelog
* Mon Jun 27 2011 Alex Burmashev <burmashev@mandriva.org> 1.0.3-3mdv2011.0
+ Revision: 687444
- Added NoDisplay=true to desktop file

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2
+ Revision: 671332
- mass rebuild

* Thu Nov 11 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 595929
- new release

* Mon Nov 09 2009 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2010.1
+ Revision: 463590
- new release

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-7mdv2009.1
+ Revision: 351033
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.0.1-6mdv2009.0
+ Revision: 218427
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-6mdv2008.1
+ Revision: 154448
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 27 2007 Funda Wang <fwang@mandriva.org> 1.0.1-5mdv2008.0
+ Revision: 72150
- fix menu entry comment

* Tue May 22 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.1-4mdv2008.0
+ Revision: 29905
- add xkill menu-entry, closes #25153
  (icons imported from mandriva 2006 package)


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:24:58 (31400)
- fill in a couple of missing descriptions

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

