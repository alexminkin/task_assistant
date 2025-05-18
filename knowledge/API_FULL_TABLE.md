| Method | URI | Name | Action | Middleware |
| ------ | --- | ---- | ------ | ---------- |
| POST | *ignition/execute-solution | ignition.executeSolution | Spatie\Lara… |  |
| GET|HEAD | _ignition/health-check | ignition.healthCheck | Spatie\LaravelIgnit… |  |
| POST | _ignition/update-config | ignition.updateConfig | Spatie\LaravelIgn… |  |
| GET|HEAD | api/v1/access/user_permissions | access.user_permissions | Modules\… |  |
| GET|HEAD | api/v1/admin/captcha/list | admin.captcha.list | Modules\Captcha\Ht… |  |
| POST | api/v1/admin/captcha/update | admin.captcha.update | Modules\Captch… |  |
| POST | api/v1/admin/company/departments | admin.company.departments.store |  |  |
| GET|HEAD | api/v1/admin/company/departments | admin.company.departments.index |  |  |
| PUT | api/v1/admin/company/departments/{department} | admin.company.depar… |  |  |
| DELETE | api/v1/admin/company/departments/{department} | admin.company.depar… |  |  |
| GET|HEAD | api/v1/admin/company/departments/{department} | admin.company.depar… |  |  |
| GET|HEAD | api/v1/admin/estate/acts | admin.estate.acts.index | Modules\Estate… |  |
| GET|HEAD | api/v1/admin/estate/acts/{id} | admin.estate.acts.show | Modules\Es… |  |
| GET|HEAD | api/v1/admin/estate/agencies | admin.estate.agencies.index | Module… |  |
| POST | api/v1/admin/estate/agencies | admin.estate.agencies.store | Module… |  |
| PUT | api/v1/admin/estate/agencies/confirm | admin.estate.agencies.confir… |  |  |
| DELETE | api/v1/admin/estate/agencies/delete_role/{id} | admin.estate.agenci… |  |  |
| GET|HEAD | api/v1/admin/estate/agencies/legal_entities | admin.estate.agencies… |  |  |
| POST | api/v1/admin/estate/agencies/legal_entities | admin.estate.agencies… |  |  |
| GET|HEAD | api/v1/admin/estate/agencies/legal_entities/show/{id} | admin.estat… |  |  |
| POST | api/v1/admin/estate/agencies/legal_entities/{id} | admin.estate.age… |  |  |
| GET|HEAD | api/v1/admin/estate/agencies/moderate_index | admin.estate.agencies… |  |  |
| POST | api/v1/admin/estate/agencies/providers/change | admin.estate.agenci… |  |  |
| GET|HEAD | api/v1/admin/estate/agencies/providers/{id} | admin.estate.agencies… |  |  |
| PUT | api/v1/admin/estate/agencies/reject | admin.estate.agencies.reject |  |  |
| GET|HEAD | api/v1/admin/estate/agencies/staff | admin.estate.agencies.staff.in… |  |  |
| POST | api/v1/admin/estate/agencies/staff | admin.estate.agencies.staff.st… |  |  |
| GET|HEAD | api/v1/admin/estate/agencies/staff/list | admin.estate.agencies.sta… |  |  |
| GET|HEAD | api/v1/admin/estate/agencies/staff/roles/{id} | admin.estate.agenci… |  |  |
| POST | api/v1/admin/estate/agencies/staff/update_roles/{id} | admin.estate… |  |  |
| POST | api/v1/admin/estate/agencies/staff/{id} | admin.estate.agencies.sta… |  |  |
| GET|HEAD | api/v1/admin/estate/agencies/staff/{id} | admin.estate.agencies.sta… |  |  |
| DELETE | api/v1/admin/estate/agencies/staff/{id} | admin.estate.agencies.sta… |  |  |
| POST | api/v1/admin/estate/agencies/update_role/{id} | admin.estate.agenci… |  |  |
| POST | api/v1/admin/estate/agencies/update_role_permissions/{id} | admin.e… |  |  |
| GET|HEAD | api/v1/admin/estate/agencies/{id} | admin.estate.agencies.show | Mo… |  |
| POST | api/v1/admin/estate/agencies/{id} | admin.estate.agencies.update | … |  |
| DELETE | api/v1/admin/estate/agencies/{id} | admin.estate.agencies.destroy |  |  |
| GET|HEAD | api/v1/admin/estate/agencies/{id}/roles | admin.estate.agencies.rol… |  |  |
| POST | api/v1/admin/estate/agencies/{id}/store_role | admin.estate.agencie… |  |  |
| POST | api/v1/admin/estate/agencies/{id}/update_access | admin.estate.agen… |  |  |
| GET|HEAD | api/v1/admin/estate/aggregator_legal_entities | admin.estate.aggreg… |  |  |
| GET|HEAD | api/v1/admin/estate/agreement_types | admin.estate.agreement_types.… |  |  |
| POST | api/v1/admin/estate/agreement_types | admin.estate.agreement_types.… |  |  |
| GET|HEAD | api/v1/admin/estate/agreement_types/{id} | admin.estate.agreement_t… |  |  |
| PUT | api/v1/admin/estate/agreement_types/{id} | admin.estate.agreement_t… |  |  |
| DELETE | api/v1/admin/estate/agreement_types/{id} | admin.estate.agreement_t… |  |  |
| GET|HEAD | api/v1/admin/estate/apartment_balconies | admin.estate.apartment_ba… |  |  |
| POST | api/v1/admin/estate/apartment_balconies | admin.estate.apartment_ba… |  |  |
| GET|HEAD | api/v1/admin/estate/apartment_balconies/{id} | admin.estate.apartme… |  |  |
| PUT | api/v1/admin/estate/apartment_balconies/{id} | admin.estate.apartme… |  |  |
| DELETE | api/v1/admin/estate/apartment_balconies/{id} | admin.estate.apartme… |  |  |
| GET|HEAD | api/v1/admin/estate/apartment_levels | admin.estate.apartment_level… |  |  |
| POST | api/v1/admin/estate/apartment_levels | admin.estate.apartment_level… |  |  |
| GET|HEAD | api/v1/admin/estate/apartment_levels/{id} | admin.estate.apartment*… |  |  |
| PUT | api/v1/admin/estate/apartment*levels/{id} | admin.estate.apartment*… |  |  |
| DELETE | api/v1/admin/estate/apartment*levels/{id} | admin.estate.apartment*… |  |  |
| GET|HEAD | api/v1/admin/estate/apartment*loggias | admin.estate.apartment_logg… |  |  |
| POST | api/v1/admin/estate/apartment_loggias | admin.estate.apartment_logg… |  |  |
| GET|HEAD | api/v1/admin/estate/apartment_loggias/{id} | admin.estate.apartment… |  |  |
| PUT | api/v1/admin/estate/apartment_loggias/{id} | admin.estate.apartment… |  |  |
| DELETE | api/v1/admin/estate/apartment_loggias/{id} | admin.estate.apartment… |  |  |
| GET|HEAD | api/v1/admin/estate/apartment_statuses | admin.estate.apartment_sta… |  |  |
| POST | api/v1/admin/estate/apartment_statuses | admin.estate.apartment_sta… |  |  |
| GET|HEAD | api/v1/admin/estate/apartment_statuses/{id} | admin.estate.apartmen… |  |  |
| PUT | api/v1/admin/estate/apartment_statuses/{id} | admin.estate.apartmen… |  |  |
| DELETE | api/v1/admin/estate/apartment_statuses/{id} | admin.estate.apartmen… |  |  |
| GET|HEAD | api/v1/admin/estate/apartment_types | admin.estate.apartment_types.… |  |  |
| POST | api/v1/admin/estate/apartment_types | admin.estate.apartment_types.… |  |  |
| GET|HEAD | api/v1/admin/estate/apartment_types/{id} | admin.estate.apartment_t… |  |  |
| PUT | api/v1/admin/estate/apartment_types/{id} | admin.estate.apartment_t… |  |  |
| DELETE | api/v1/admin/estate/apartment_types/{id} | admin.estate.apartment_t… |  |  |
| GET|HEAD | api/v1/admin/estate/apartments | admin.estate.apartments.index | Mo… |  |
| POST | api/v1/admin/estate/apartments | admin.estate.apartments.store | Mo… |  |
| POST | api/v1/admin/estate/apartments/multi-store | admin.estate.apartment… |  |  |
| GET|HEAD | api/v1/admin/estate/apartments/{id} | admin.estate.apartments.show |  |  |
| POST | api/v1/admin/estate/apartments/{id} | admin.estate.apartments.updat… |  |  |
| DELETE | api/v1/admin/estate/apartments/{id} | admin.estate.apartments.destr… |  |  |
| GET|HEAD | api/v1/admin/estate/banks | admin.estate.banks.index | Modules\Esta… |  |
| POST | api/v1/admin/estate/banks | admin.estate.banks.store | Modules\Esta… |  |
| GET|HEAD | api/v1/admin/estate/banks/{id} | admin.estate.banks.show | Modules\… |  |
| POST | api/v1/admin/estate/banks/{id} | admin.estate.banks.update | Module… |  |
| DELETE | api/v1/admin/estate/banks/{id} | admin.estate.banks.destroy | Modul… |  |
| GET|HEAD | api/v1/admin/estate/calculation_indicators | admin.estate.calculati… |  |  |
| GET|HEAD | api/v1/admin/estate/calculation_indicators/{id} | admin.estate.calc… |  |  |
| GET|HEAD | api/v1/admin/estate/calculation_methods | admin.estate.calculation*… |  |  |
| GET|HEAD | api/v1/admin/estate/calculation*methods/{id} | admin.estate.calcula… |  |  |
| GET|HEAD | api/v1/admin/estate/calculation_months | admin.estate.calculation_m… |  |  |
| GET|HEAD | api/v1/admin/estate/calculation_months/{id} | admin.estate.calculat… |  |  |
| GET|HEAD | api/v1/admin/estate/clients | admin.estate.clients.index | Modules\… |  |
| POST | api/v1/admin/estate/clients | admin.estate.clients.store | Modules\… |  |
| GET|HEAD | api/v1/admin/estate/clients/{id} | admin.estate.clients.show | Modu… |  |
| POST | api/v1/admin/estate/clients/{id} | admin.estate.clients.update | Mo… |  |
| DELETE | api/v1/admin/estate/clients/{id} | admin.estate.clients.destroy | M… |  |
| GET|HEAD | api/v1/admin/estate/clients/{id}/deals | admin.estate.clients.index… |  |  |
| GET|HEAD | api/v1/admin/estate/clients/{id}/history | admin.estate.clients.ind… |  |  |
| GET|HEAD | api/v1/admin/estate/curators | admin.estate.curators.index | Module… |  |
| POST | api/v1/admin/estate/curators | admin.estate.curators.store | Module… |  |
| GET|HEAD | api/v1/admin/estate/curators/list | admin.estate.curators.list | Mo… |  |
| GET|HEAD | api/v1/admin/estate/curators/{id} | admin.estate.curators.show | Mo… |  |
| POST | api/v1/admin/estate/curators/{id} | admin.estate.curators.update | … |  |
| DELETE | api/v1/admin/estate/curators/{id} | admin.estate.curators.destroy |  |  |
| GET|HEAD | api/v1/admin/estate/deal_types | admin.estate.deal_types.index | Mo… |  |
| POST | api/v1/admin/estate/deal_types | admin.estate.deal_types.store | Mo… |  |
| GET|HEAD | api/v1/admin/estate/deal_types/{id} | admin.estate.deal_types.show |  |  |
| PUT | api/v1/admin/estate/deal_types/{id} | admin.estate.deal_types.updat… |  |  |
| DELETE | api/v1/admin/estate/deal_types/{id} | admin.estate.deal_types.destr… |  |  |
| GET|HEAD | api/v1/admin/estate/deals | admin.estate.deals.index | Modules\Esta… |  |
| GET|HEAD | api/v1/admin/estate/deals/stages | admin.estate.deals.stages | Modu… |  |
| GET|HEAD | api/v1/admin/estate/deals/statuses | admin.estate.deals.statuses | … |  |
| GET|HEAD | api/v1/admin/estate/deals/{id} | admin.estate.deals.show | Modules\… |  |
| POST | api/v1/admin/estate/deals/{id} | admin.estate.deals.update | Module… |  |
| GET|HEAD | api/v1/admin/estate/deals/{id}/clients | admin.estate.deals.indexCl… |  |  |
| GET|HEAD | api/v1/admin/estate/deals/{id}/history | admin.estate.deals.indexHi… |  |  |
| GET|HEAD | api/v1/admin/estate/deals/{id}/regulations | admin.estate.deals.reg… |  |  |
| GET|HEAD | api/v1/admin/estate/decoration_types | admin.estate.decoration_type… |  |  |
| POST | api/v1/admin/estate/decoration_types | admin.estate.decoration_type… |  |  |
| GET|HEAD | api/v1/admin/estate/decoration_types/{id} | admin.estate.decoration… |  |  |
| POST | api/v1/admin/estate/decoration_types/{id} | admin.estate.decoration… |  |  |
| DELETE | api/v1/admin/estate/decoration_types/{id} | admin.estate.decoration… |  |  |
| GET|HEAD | api/v1/admin/estate/developers | admin.estate.developers.index | Mo… |  |
| POST | api/v1/admin/estate/developers | admin.estate.developers.store | Mo… |  |
| GET|HEAD | api/v1/admin/estate/developers/{id} | admin.estate.developers.show |  |  |
| PUT | api/v1/admin/estate/developers/{id} | admin.estate.developers.updat… |  |  |
| DELETE | api/v1/admin/estate/developers/{id} | admin.estate.developers.destr… |  |  |
| GET|HEAD | api/v1/admin/estate/districts | admin.estate.districts.index | Modu… |  |
| POST | api/v1/admin/estate/districts | admin.estate.districts.store | Modu… |  |
| GET|HEAD | api/v1/admin/estate/districts/{id} | admin.estate.districts.show | … |  |
| PUT | api/v1/admin/estate/districts/{id} | admin.estate.districts.update |  |  |
| DELETE | api/v1/admin/estate/districts/{id} | admin.estate.districts.destroy… |  |  |
| GET|HEAD | api/v1/admin/estate/elevator_types | admin.estate.elevator_types.in… |  |  |
| POST | api/v1/admin/estate/elevator_types | admin.estate.elevator_types.st… |  |  |
| GET|HEAD | api/v1/admin/estate/elevator_types/{id} | admin.estate.elevator_typ… |  |  |
| PUT | api/v1/admin/estate/elevator_types/{id} | admin.estate.elevator_typ… |  |  |
| DELETE | api/v1/admin/estate/elevator_types/{id} | admin.estate.elevator_typ… |  |  |
| POST | api/v1/admin/estate/entrances | admin.estate.entrances.store | Modu… |  |
| GET|HEAD | api/v1/admin/estate/entrances/index/{estate_id} | admin.estate.entr… |  |  |
| GET|HEAD | api/v1/admin/estate/entrances/{id} | admin.estate.entrances.show | … |  |
| POST | api/v1/admin/estate/entrances/{id} | admin.estate.entrances.update |  |  |
| DELETE | api/v1/admin/estate/entrances/{id} | admin.estate.entrances.destroy… |  |  |
| GET|HEAD | api/v1/admin/estate/estate_object_types | admin.estate.estate_objec… |  |  |
| GET|HEAD | api/v1/admin/estate/estate_payment_methods | admin.estate.estate_pa… |  |  |
| POST | api/v1/admin/estate/estate_payment_methods | admin.estate.estate_pa… |  |  |
| GET|HEAD | api/v1/admin/estate/estate_payment_methods/{id} | admin.estate.esta… |  |  |
| PUT | api/v1/admin/estate/estate_payment_methods/{id} | admin.estate.esta… |  |  |
| DELETE | api/v1/admin/estate/estate_payment_methods/{id} | admin.estate.esta… |  |  |
| GET|HEAD | api/v1/admin/estate/estate_payment_types | admin.estate.estate_paym… |  |  |
| POST | api/v1/admin/estate/estate_payment_types | admin.estate.estate_paym… |  |  |
| GET|HEAD | api/v1/admin/estate/estate_payment_types/{id} | admin.estate.estate… |  |  |
| PUT | api/v1/admin/estate/estate_payment_types/{id} | admin.estate.estate… |  |  |
| DELETE | api/v1/admin/estate/estate_payment_types/{id} | admin.estate.estate… |  |  |
| GET|HEAD | api/v1/admin/estate/estate_types | admin.estate.estate_types.index |  |  |
| POST | api/v1/admin/estate/estate_types | admin.estate.estate_types.store |  |  |
| GET|HEAD | api/v1/admin/estate/estate_types/{id} | admin.estate.estate_types.s… |  |  |
| PUT | api/v1/admin/estate/estate_types/{id} | admin.estate.estate_types.u… |  |  |
| DELETE | api/v1/admin/estate/estate_types/{id} | admin.estate.estate_types.d… |  |  |
| GET|HEAD | api/v1/admin/estate/estates | admin.estate.estates.index | Modules\… |  |
| POST | api/v1/admin/estate/estates | admin.estate.estates.store | Modules\… |  |
| GET|HEAD | api/v1/admin/estate/estates/export | admin.estate.estates.export | … |  |
| POST | api/v1/admin/estate/estates/recount_params/{id} | admin.estate.esta… |  |  |
| GET|HEAD | api/v1/admin/estate/estates/{id} | admin.estate.estates.show | Modu… |  |
| POST | api/v1/admin/estate/estates/{id} | admin.estate.estates.update | Mo… |  |
| DELETE | api/v1/admin/estate/estates/{id} | admin.estate.estates.destroy | M… |  |
| GET|HEAD | api/v1/admin/estate/hc_classes | admin.estate.hc_classes.index | Mo… |  |
| POST | api/v1/admin/estate/hc_classes | admin.estate.hc_classes.store | Mo… |  |
| GET|HEAD | api/v1/admin/estate/hc_classes/{id} | admin.estate.hc_classes.show |  |  |
| PUT | api/v1/admin/estate/hc_classes/{id} | admin.estate.hc_classes.updat… |  |  |
| DELETE | api/v1/admin/estate/hc_classes/{id} | admin.estate.hc_classes.destr… |  |  |
| GET|HEAD | api/v1/admin/estate/hc_document_types | admin.estate.hc_document_ty… |  |  |
| POST | api/v1/admin/estate/hc_document_types | admin.estate.hc_document_ty… |  |  |
| GET|HEAD | api/v1/admin/estate/hc_document_types/{id} | admin.estate.hc_docume… |  |  |
| PUT | api/v1/admin/estate/hc_document_types/{id} | admin.estate.hc_docume… |  |  |
| DELETE | api/v1/admin/estate/hc_document_types/{id} | admin.estate.hc_docume… |  |  |
| GET|HEAD | api/v1/admin/estate/hc_parsing_statuses | admin.estate.hc_parsing_s… |  |  |
| GET|HEAD | api/v1/admin/estate/hc_special_statuses | admin.estate.hc_special_s… |  |  |
| POST | api/v1/admin/estate/hc_special_statuses | admin.estate.hc_special_s… |  |  |
| GET|HEAD | api/v1/admin/estate/hc_special_statuses/{id} | admin.estate.hc_spec… |  |  |
| PUT | api/v1/admin/estate/hc_special_statuses/{id} | admin.estate.hc_spec… |  |  |
| DELETE | api/v1/admin/estate/hc_special_statuses/{id} | admin.estate.hc_spec… |  |  |
| GET|HEAD | api/v1/admin/estate/hc_types | admin.estate.hc_types.index | Module… |  |
| POST | api/v1/admin/estate/hc_types | admin.estate.hc_types.store | Module… |  |
| GET|HEAD | api/v1/admin/estate/hc_types/{id} | admin.estate.hc_types.show | Mo… |  |
| PUT | api/v1/admin/estate/hc_types/{id} | admin.estate.hc_types.update | … |  |
| DELETE | api/v1/admin/estate/hc_types/{id} | admin.estate.hc_types.destroy |  |  |
| GET|HEAD | api/v1/admin/estate/history | admin.estate.history.index | Modules\… |  |
| GET|HEAD | api/v1/admin/estate/housing_complexes | admin.estate.housing_comple… |  |  |
| POST | api/v1/admin/estate/housing_complexes | admin.estate.housing_comple… |  |  |
| PUT | api/v1/admin/estate/housing_complexes/fast-update/{id} | admin.esta… |  |  |
| GET|HEAD | api/v1/admin/estate/housing_complexes/{id} | admin.estate.housing_c… |  |  |
| POST | api/v1/admin/estate/housing_complexes/{id} | admin.estate.housing_c… |  |  |
| DELETE | api/v1/admin/estate/housing_complexes/{id} | admin.estate.housing_c… |  |  |
| GET|HEAD | api/v1/admin/estate/infrastructures | admin.estate.infrastructures.… |  |  |
| POST | api/v1/admin/estate/infrastructures | admin.estate.infrastructures.… |  |  |
| GET|HEAD | api/v1/admin/estate/infrastructures/{id} | admin.estate.infrastruct… |  |  |
| PUT | api/v1/admin/estate/infrastructures/{id} | admin.estate.infrastruct… |  |  |
| DELETE | api/v1/admin/estate/infrastructures/{id} | admin.estate.infrastruct… |  |  |
| GET|HEAD | api/v1/admin/estate/metro_lines | admin.estate.metro_lines.index | … |  |
| POST | api/v1/admin/estate/metro_lines | admin.estate.metro_lines.store | … |  |
| GET|HEAD | api/v1/admin/estate/metro_lines/{id} | admin.estate.metro_lines.sho… |  |  |
| PUT | api/v1/admin/estate/metro_lines/{id} | admin.estate.metro_lines.upd… |  |  |
| DELETE | api/v1/admin/estate/metro_lines/{id} | admin.estate.metro_lines.des… |  |  |
| GET|HEAD | api/v1/admin/estate/metro_ways | admin.estate.metro_ways.index | Mo… |  |
| GET|HEAD | api/v1/admin/estate/metro_ways/{alias} | admin.estate.metro_ways.sh… |  |  |
| GET|HEAD | api/v1/admin/estate/metros | admin.estate.metros.index | Modules\Es… |  |
| POST | api/v1/admin/estate/metros | admin.estate.metros.store | Modules\Es… |  |
| GET|HEAD | api/v1/admin/estate/metros/{id} | admin.estate.metros.show | Module… |  |
| PUT | api/v1/admin/estate/metros/{id} | admin.estate.metros.update | Modu… |  |
| DELETE | api/v1/admin/estate/metros/{id} | admin.estate.metros.destroy | Mod… |  |
| GET|HEAD | api/v1/admin/estate/parking_locations | admin.estate.parking_locati… |  |  |
| POST | api/v1/admin/estate/parking_locations | admin.estate.parking_locati… |  |  |
| GET|HEAD | api/v1/admin/estate/parking_locations/{id} | admin.estate.parking_l… |  |  |
| PUT | api/v1/admin/estate/parking_locations/{id} | admin.estate.parking_l… |  |  |
| DELETE | api/v1/admin/estate/parking_locations/{id} | admin.estate.parking_l… |  |  |
| GET|HEAD | api/v1/admin/estate/parking_types | admin.estate.parking_types.inde… |  |  |
| POST | api/v1/admin/estate/parking_types | admin.estate.parking_types.stor… |  |  |
| GET|HEAD | api/v1/admin/estate/parking_types/{id} | admin.estate.parking_types… |  |  |
| PUT | api/v1/admin/estate/parking_types/{id} | admin.estate.parking_types… |  |  |
| DELETE | api/v1/admin/estate/parking_types/{id} | admin.estate.parking_types… |  |  |
| GET|HEAD | api/v1/admin/estate/patios | admin.estate.patios.index | Modules\Es… |  |
| POST | api/v1/admin/estate/patios | admin.estate.patios.store | Modules\Es… |  |
| GET|HEAD | api/v1/admin/estate/patios/{id} | admin.estate.patios.show | Module… |  |
| PUT | api/v1/admin/estate/patios/{id} | admin.estate.patios.update | Modu… |  |
| DELETE | api/v1/admin/estate/patios/{id} | admin.estate.patios.destroy | Mod… |  |
| GET|HEAD | api/v1/admin/estate/providers | admin.estate.providers.index | Modu… |  |
| POST | api/v1/admin/estate/providers | admin.estate.providers.store | Modu… |  |
| GET|HEAD | api/v1/admin/estate/providers/{id} | admin.estate.providers.show | … |  |
| PUT | api/v1/admin/estate/providers/{id} | admin.estate.providers.update |  |  |
| DELETE | api/v1/admin/estate/providers/{id} | admin.estate.providers.destroy… |  |  |
| GET|HEAD | api/v1/admin/estate/regulation_tariff_cards | admin.estate.regulati… |  |  |
| POST | api/v1/admin/estate/regulation_tariff_cards | admin.estate.regulati… |  |  |
| GET|HEAD | api/v1/admin/estate/regulation_tariff_cards/{id} | admin.estate.reg… |  |  |
| PUT | api/v1/admin/estate/regulation_tariff_cards/{id} | admin.estate.reg… |  |  |
| GET|HEAD | api/v1/admin/estate/regulations | admin.estate.regulations.index | … |  |
| POST | api/v1/admin/estate/regulations | admin.estate.regulations.store | … |  |
| GET|HEAD | api/v1/admin/estate/regulations/{id} | admin.estate.regulations.sho… |  |  |
| PUT | api/v1/admin/estate/regulations/{id} | admin.estate.regulations.upd… |  |  |
| GET|HEAD | api/v1/admin/estate/room_types | admin.estate.room_types.index | Mo… |  |
| POST | api/v1/admin/estate/room_types | admin.estate.room_types.store | Mo… |  |
| GET|HEAD | api/v1/admin/estate/room_types/{id} | admin.estate.room_types.show |  |  |
| PUT | api/v1/admin/estate/room_types/{id} | admin.estate.room_types.updat… |  |  |
| DELETE | api/v1/admin/estate/room_types/{id} | admin.estate.room_types.destr… |  |  |
| GET|HEAD | api/v1/admin/estate/terraces | admin.estate.terraces.index | Module… |  |
| POST | api/v1/admin/estate/terraces | admin.estate.terraces.store | Module… |  |
| GET|HEAD | api/v1/admin/estate/terraces/{id} | admin.estate.terraces.show | Mo… |  |
| PUT | api/v1/admin/estate/terraces/{id} | admin.estate.terraces.update | … |  |
| DELETE | api/v1/admin/estate/terraces/{id} | admin.estate.terraces.destroy |  |  |
| GET|HEAD | api/v1/admin/estate/verandas | admin.estate.verandas.index | Module… |  |
| POST | api/v1/admin/estate/verandas | admin.estate.verandas.store | Module… |  |
| GET|HEAD | api/v1/admin/estate/verandas/{id} | admin.estate.verandas.show | Mo… |  |
| PUT | api/v1/admin/estate/verandas/{id} | admin.estate.verandas.update | … |  |
| DELETE | api/v1/admin/estate/verandas/{id} | admin.estate.verandas.destroy |  |  |
| POST | api/v1/admin/faq/answers | admin.faq.answers.store | Modules\Faq\Ht… |  |
| GET|HEAD | api/v1/admin/faq/answers | admin.faq.answers.index | Modules\Faq\Ht… |  |
| DELETE | api/v1/admin/faq/answers/{answer} | admin.faq.answers.delete | Modu… |  |
| PATCH | api/v1/admin/faq/answers/{id} | admin.faq.answers.update | Modules\… |  |
| GET|HEAD | api/v1/admin/faq/answers/{id} | admin.faq.answers.show | Modules\Fa… |  |
| POST | api/v1/admin/faq/categories | admin.faq.categories.store | Modules\… |  |
| GET|HEAD | api/v1/admin/faq/categories | admin.faq.categories.index | Modules\… |  |
| DELETE | api/v1/admin/faq/categories/{category} | admin.faq.categories.delet… |  |  |
| PATCH | api/v1/admin/faq/categories/{id} | admin.faq.categories.update | Mo… |  |
| GET|HEAD | api/v1/admin/faq/categories/{id} | admin.faq.categories.show | Modu… |  |
| POST | api/v1/admin/faq/questions | admin.faq.questions.store | Modules\Fa… |  |
| GET|HEAD | api/v1/admin/faq/questions | admin.faq.questions.index | Modules\Fa… |  |
| GET|HEAD | api/v1/admin/faq/questions/export | admin.faq.questions.export | Mo… |  |
| PATCH | api/v1/admin/faq/questions/{id} | admin.faq.questions.update | Modu… |  |
| GET|HEAD | api/v1/admin/faq/questions/{id} | admin.faq.questions.show | Module… |  |
| DELETE | api/v1/admin/faq/questions/{question} | admin.faq.questions.delete |  |  |
| GET|HEAD | api/v1/admin/feedback/queries | admin.feedback.queries.index | Modu… |  |
| POST | api/v1/admin/feedback/queries/batch-status-update | admin.feedback.… |  |  |
| GET|HEAD | api/v1/admin/feedback/queries/export | admin.feedback.queries.expor… |  |  |
| GET|HEAD | api/v1/admin/feedback/queries/statuses | admin.feedback.queries.sta… |  |  |
| GET|HEAD | api/v1/admin/feedback/queries/{feedbackQuery} | admin.feedback.quer… |  |  |
| PATCH | api/v1/admin/feedback/queries/{feedbackQuery} | admin.feedback.quer… |  |  |
| DELETE | api/v1/admin/feedback/queries/{feedbackQuery} | admin.feedback.quer… |  |  |
| GET|HEAD | api/v1/admin/feedback/query-themes | admin.feedback.query_themes.in… |  |  |
| POST | api/v1/admin/feedback/query-themes | admin.feedback.query_themes.st… |  |  |
| PUT | api/v1/admin/feedback/query-themes/{feedbackQueryTheme} | admin.fee… |  |  |
| DELETE | api/v1/admin/feedback/query-themes/{feedbackQueryTheme} | admin.fee… |  |  |
| GET|HEAD | api/v1/admin/feedback/reviews | admin.feedback.reviews.index | Modu… |  |
| POST | api/v1/admin/feedback/reviews/batch-status-update | admin.feedback.… |  |  |
| GET|HEAD | api/v1/admin/feedback/reviews/export | admin.feedback.reviews.expor… |  |  |
| GET|HEAD | api/v1/admin/feedback/reviews/statuses | admin.feedback.reviews.sta… |  |  |
| GET|HEAD | api/v1/admin/feedback/reviews/{feedbackReview} | admin.feedback.rev… |  |  |
| PATCH | api/v1/admin/feedback/reviews/{feedbackReview} | admin.feedback.rev… |  |  |
| DELETE | api/v1/admin/feedback/reviews/{feedbackReview} | admin.feedback.rev… |  |  |
| PUT | api/v1/admin/feedback/settings | admin.feedback.settings.update | M… |  |
| GET|HEAD | api/v1/admin/feedback/settings/form-fields | admin.feedback.setting… |  |  |
| GET|HEAD | api/v1/admin/feedback/settings/form-groups | admin.feedback.setting… |  |  |
| GET|HEAD | api/v1/admin/feedback/stats | admin.feedback.stats | Modules\Feedba… |  |
| GET|HEAD | api/v1/admin/finance/account-purpose-list | admin.finance.lists.acc… |  |  |
| GET|HEAD | api/v1/admin/finance/account-summary | admin.finance.lists.account*… |  |  |
| GET|HEAD | api/v1/admin/finance/company-accounts | admin.finance.company*accou… |  |  |
| GET|HEAD | api/v1/admin/finance/currencies | admin.finance.currencies.index | … |  |
| POST | api/v1/admin/finance/currencies | admin.finance.currencies.store | … |  |
| PATCH | api/v1/admin/finance/currencies/{currency} | admin.finance.currenci… |  |  |
| GET|HEAD | api/v1/admin/finance/currencies/{currency} | admin.finance.currenci… |  |  |
| GET|HEAD | api/v1/admin/finance/document-status-list | admin.finance.lists.doc… |  |  |
| GET|HEAD | api/v1/admin/finance/document-type-list | admin.finance.lists.docum… |  |  |
| GET|HEAD | api/v1/admin/finance/documents | admin.finance.documents.index | Mo… |  |
| GET|HEAD | api/v1/admin/finance/documents/export | admin.finance.documents.exp… |  |  |
| PATCH | api/v1/admin/finance/documents/{document} | admin.finance.documents… |  |  |
| GET|HEAD | api/v1/admin/finance/documents/{document}/objects | admin.finance.d… |  |  |
| POST | api/v1/admin/finance/documents/{document}/post | admin.finance.docu… |  |  |
| POST | api/v1/admin/finance/documents/{document}/reject | admin.finance.do… |  |  |
| GET|HEAD | api/v1/admin/finance/documents/{document}/related-documents | admin… |  |  |
| GET|HEAD | api/v1/admin/finance/documents/{document}/transactions | admin.fina… |  |  |
| GET|HEAD | api/v1/admin/finance/object-types | admin.finance.lists.object_type… |  |  |
| GET|HEAD | api/v1/admin/finance/operated-currency-list | admin.finance.lists.o… |  |  |
| POST | api/v1/admin/finance/operations/company-expense | admin.finance.ope… |  |  |
| GET|HEAD | api/v1/admin/finance/operations/company-expense/credit-accounts | a… |  |  |
| GET|HEAD | api/v1/admin/finance/operations/company-expense/debit-purposes | ad… |  |  |
| POST | api/v1/admin/finance/operations/company-replenishment | admin.finan… |  |  |
| GET|HEAD | api/v1/admin/finance/operations/company-replenishment/credit-purposes | admin.finance.operations.company_replenishment.credit_purposes.index | Modules\Finance\Http\Controllers\Api\V1\Admin\CompanyReplenishment\CreditPurposeController@… |  |
| GET|HEAD | api/v1/admin/finance/operations/company-replenishment/debit-accounts | admin.finance.operations.company_replenishment.debit_accounts.index | Modules\Finance\Http\Controllers\Api\V1\Admin\CompanyReplenishment\DebitAccountController@i… |  |
| POST | api/v1/admin/finance/operations/user-transfer | admin.finance.opera… |  |  |
| GET|HEAD | api/v1/admin/finance/operations/user-transfer/credit-accounts | adm… |  |  |
| POST | api/v1/admin/finance/operations/user-withdrawal | admin.finance.ope… |  |  |
| GET|HEAD | api/v1/admin/finance/operations/user-withdrawal/debit-accounts | ad… |  |  |
| GET|HEAD | api/v1/admin/finance/rates | admin.finance.rates.index | Modules\Fi… |  |
| GET|HEAD | api/v1/admin/finance/rates/service-list | admin.finance.rates.servi… |  |  |
| PUT | api/v1/admin/finance/rates/{id} | admin.finance.rates.update | Modu… |  |
| GET|HEAD | api/v1/admin/finance/third-party-list | admin.finance.lists.third_p… |  |  |
| GET|HEAD | api/v1/admin/finance/transaction-type-list | admin.finance.lists.tr… |  |  |
| GET|HEAD | api/v1/admin/finance/transactions | admin.finance.transactions.inde… |  |  |
| GET|HEAD | api/v1/admin/finance/transactions/export | admin.finance.transactio… |  |  |
| GET|HEAD | api/v1/admin/finance/user-accounts | admin.finance.user_accounts.in… |  |  |
| GET|HEAD | api/v1/admin/finance/user-accounts/export | admin.finance.user_acco… |  |  |
| PATCH | api/v1/admin/finance/user-accounts/{account} | admin.finance.user_a… |  |  |
| GET|HEAD | api/v1/admin/finance/user-purpose-settings | admin.finance.user_pur… |  |  |
| PUT | api/v1/admin/finance/user-purpose-settings | admin.finance.user_pur… |  |  |
| GET|HEAD | api/v1/admin/marketing | admin.marketing.index | Modules\Marketing\… |  |
| POST | api/v1/admin/marketing | admin.marketing.store | Modules\Marketing\… |  |
| GET|HEAD | api/v1/admin/marketing/activity | admin.marketing.activity.index | … |  |
| PUT | api/v1/admin/marketing/activity | admin.marketing.activity.update |  |  |
| GET|HEAD | api/v1/admin/marketing/activity/activity-condition-list | admin.mar… |  |  |
| GET|HEAD | api/v1/admin/marketing/activity/conditions | admin.marketing.activi… |  |  |
| PUT | api/v1/admin/marketing/activity/conditions/{id} | admin.marketing.a… |  |  |
| GET|HEAD | api/v1/admin/marketing/advanced-stats | admin.marketing.advanced-st… |  |  |
| GET|HEAD | api/v1/admin/marketing/bonuses | admin.marketing.bonuses.index | Mo… |  |
| GET|HEAD | api/v1/admin/marketing/bonuses/bonuses-for-matching/{periodTypeId} | admin.marketing.bonuses.bonuses_for_matching | Modules\Marketing\Http\Controllers\Api\V1\Admin\BonusController@bonusesForMatchi… |  |
| POST | api/v1/admin/marketing/bonuses/cashback | admin.marketing.bonuses.s… |  |  |
| PUT | api/v1/admin/marketing/bonuses/cashback/{bonus} | admin.marketing.b… |  |  |
| GET|HEAD | api/v1/admin/marketing/bonuses/conditions | admin.marketing.bonuses… |  |  |
| GET|HEAD | api/v1/admin/marketing/bonuses/events | admin.marketing.bonuses.eve… |  |  |
| POST | api/v1/admin/marketing/bonuses/matching | admin.marketing.bonuses.s… |  |  |
| PUT | api/v1/admin/marketing/bonuses/matching/{bonus} | admin.marketing.b… |  |  |
| POST | api/v1/admin/marketing/bonuses/rank | admin.marketing.bonuses.store… |  |  |
| PUT | api/v1/admin/marketing/bonuses/rank/{bonus} | admin.marketing.bonus… |  |  |
| POST | api/v1/admin/marketing/bonuses/referral | admin.marketing.bonuses.s… |  |  |
| PUT | api/v1/admin/marketing/bonuses/referral/{bonus} | admin.marketing.b… |  |  |
| POST | api/v1/admin/marketing/bonuses/small-branch | admin.marketing.bonus… |  |  |
| PUT | api/v1/admin/marketing/bonuses/small-branch/{bonus} | admin.marketi… |  |  |
| POST | api/v1/admin/marketing/bonuses/stage | admin.marketing.bonuses.stor… |  |  |
| PUT | api/v1/admin/marketing/bonuses/stage/{bonus} | admin.marketing.bonu… |  |  |
| POST | api/v1/admin/marketing/bonuses/step | admin.marketing.bonuses.store… |  |  |
| PUT | api/v1/admin/marketing/bonuses/step/{bonus} | admin.marketing.bonus… |  |  |
| GET|HEAD | api/v1/admin/marketing/bonuses/types | admin.marketing.bonuses.type… |  |  |
| GET|HEAD | api/v1/admin/marketing/bonuses/{bonus} | admin.marketing.bonuses.sh… |  |  |
| PUT | api/v1/admin/marketing/bonuses/{id} | admin.marketing.bonuses.updat… |  |  |
| DELETE | api/v1/admin/marketing/bonuses/{id} | admin.marketing.bonuses.destr… |  |  |
| GET|HEAD | api/v1/admin/marketing/calendar-period-list | admin.marketing.calen… |  |  |
| GET|HEAD | api/v1/admin/marketing/communication-method-list | admin.marketing.… |  |  |
| PUT | api/v1/admin/marketing/help | admin.marketing.help | Modules\Market… |  |
| GET|HEAD | api/v1/admin/marketing/lists/packages | admin.marketing.lists.packa… |  |  |
| GET|HEAD | api/v1/admin/marketing/lists/ranks | admin.marketing.lists.ranks | … |  |
| GET|HEAD | api/v1/admin/marketing/packages | admin.marketing.packages.index | … |  |
| POST | api/v1/admin/marketing/packages | admin.marketing.packages.store | … |  |
| GET|HEAD | api/v1/admin/marketing/packages/settings | admin.marketing.packages… |  |  |
| PATCH | api/v1/admin/marketing/packages/settings | admin.marketing.packages… |  |  |
| GET|HEAD | api/v1/admin/marketing/packages/settings/package-type-list | admin.… |  |  |
| GET|HEAD | api/v1/admin/marketing/packages/{package} | admin.marketing.package… |  |  |
| PATCH | api/v1/admin/marketing/packages/{package} | admin.marketing.package… |  |  |
| DELETE | api/v1/admin/marketing/packages/{package} | admin.marketing.package… |  |  |
| GET|HEAD | api/v1/admin/marketing/periods | admin.marketing.periods.index | Mo… |  |
| POST | api/v1/admin/marketing/periods | admin.marketing.periods.store | Mo… |  |
| GET|HEAD | api/v1/admin/marketing/periods/period-type-list | admin.marketing.p… |  |  |
| GET|HEAD | api/v1/admin/marketing/periods/period-type-status-list | admin.mark… |  |  |
| GET|HEAD | api/v1/admin/marketing/periods/{id} | admin.marketing.periods.show |  |  |
| PUT | api/v1/admin/marketing/periods/{id} | admin.marketing.periods.updat… |  |  |
| DELETE | api/v1/admin/marketing/periods/{id} | admin.marketing.periods.destr… |  |  |
| GET|HEAD | api/v1/admin/marketing/prepared | admin.marketing.prepared.index | … |  |
| GET|HEAD | api/v1/admin/marketing/prepared/{plan} | admin.marketing.prepared.s… |  |  |
| POST | api/v1/admin/marketing/prepared/{plan}/up | admin.marketing.prepare… |  |  |
| GET|HEAD | api/v1/admin/marketing/ranks | admin.marketing.ranks.index | Module… |  |
| POST | api/v1/admin/marketing/ranks | admin.marketing.ranks.store | Module… |  |
| GET|HEAD | api/v1/admin/marketing/ranks/rank-condition-list | admin.marketing.… |  |  |
| GET|HEAD | api/v1/admin/marketing/ranks/rank-list/{id?} | admin.marketing.rank… |  |  |
| GET|HEAD | api/v1/admin/marketing/ranks/{id} | admin.marketing.ranks.show | Mo… |  |
| PUT | api/v1/admin/marketing/ranks/{id} | admin.marketing.ranks.update | … |  |
| DELETE | api/v1/admin/marketing/ranks/{id} | admin.marketing.ranks.destroy |  |  |
| GET|HEAD | api/v1/admin/marketing/reports/bonus-payment | admin.marketing.repo… |  |  |
| GET|HEAD | api/v1/admin/marketing/reports/profitability | admin.marketing.repo… |  |  |
| GET|HEAD | api/v1/admin/marketing/reports/profitability/export | admin.marketi… |  |  |
| GET|HEAD | api/v1/admin/marketing/stats | admin.marketing.stats | Modules\Mark… |  |
| GET|HEAD | api/v1/admin/marketing/status-list | admin.marketing.status_list | … |  |
| GET|HEAD | api/v1/admin/marketing/structures | admin.marketing.structures.inde… |  |  |
| POST | api/v1/admin/marketing/structures | admin.marketing.structures.stor… |  |  |
| GET|HEAD | api/v1/admin/marketing/structures/filling-event-list | admin.market… |  |  |
| GET|HEAD | api/v1/admin/marketing/structures/filling-type-list | admin.marketi… |  |  |
| GET|HEAD | api/v1/admin/marketing/structures/for-step-bonus-list/{bonusId?} | … |  |  |
| GET|HEAD | api/v1/admin/marketing/structures/infinity | admin.marketing.struct… |  |  |
| GET|HEAD | api/v1/admin/marketing/structures/{structure_type} | admin.marketin… |  |  |
| PATCH | api/v1/admin/marketing/structures/{structure_type} | admin.marketin… |  |  |
| DELETE | api/v1/admin/marketing/structures/{structure_type} | admin.marketin… |  |  |
| GET|HEAD | api/v1/admin/marketing/volumes | admin.marketing.volumes.index | Mo… |  |
| GET|HEAD | api/v1/admin/marketing/volumes/volume-condition-list | admin.market… |  |  |
| GET|HEAD | api/v1/admin/marketing/volumes/{volume} | admin.marketing.volumes.s… |  |  |
| PATCH | api/v1/admin/marketing/volumes/{volume} | admin.marketing.volumes.u… |  |  |
| DELETE | api/v1/admin/marketing/{marketing} | admin.marketing.destroy | Modu… |  |
| GET|HEAD | api/v1/admin/marketing/{marketing} | admin.marketing.show | Modules… |  |
| PUT | api/v1/admin/marketing/{marketing} | admin.marketing.update | Modul… |  |
| PATCH | api/v1/admin/marketing/{marketing}/complete | admin.marketing.compl… |  |  |
| POST | api/v1/admin/marketing/{marketing}/copy | admin.marketing.copy | Mo… |  |
| GET|HEAD | api/v1/admin/news | admin.news.index | Modules\CustomConfig\Http\Co… |  |
| POST | api/v1/admin/news | admin.news.store | Modules\CustomConfig\Http\Co… |  |
| GET|HEAD | api/v1/admin/news/categories | admin.news.categories.index | Module… |  |
| POST | api/v1/admin/news/categories | admin.news.categories.store | Module… |  |
| GET|HEAD | api/v1/admin/news/categories/{id} | admin.news.categories.show | Mo… |  |
| PATCH | api/v1/admin/news/categories/{id} | admin.news.categories.update | … |  |
| DELETE | api/v1/admin/news/categories/{id} | admin.news.categories.destroy |  |  |
| GET|HEAD | api/v1/admin/news/{id} | admin.news.show | Modules\CustomConfig\Htt… |  |
| PATCH | api/v1/admin/news/{id} | admin.news.update | Modules\CustomConfig\H… |  |
| DELETE | api/v1/admin/news/{id} | admin.news.destroy | Modules\News\Http\Con… |  |
| GET|HEAD | api/v1/admin/notification/history | admin.notification.history.inde… |  |  |
| GET|HEAD | api/v1/admin/notification/history/channels | admin.notification.his… |  |  |
| GET|HEAD | api/v1/admin/notification/history/export | admin.notification.histo… |  |  |
| GET|HEAD | api/v1/admin/notification/history/providers | admin.notification.hi… |  |  |
| GET|HEAD | api/v1/admin/payment-systems | admin.payment_systems.index | Module… |  |
| POST | api/v1/admin/payment-systems | admin.payment_systems.store | Module… |  |
| GET|HEAD | api/v1/admin/payment-systems/commission-type-list | admin.payment_s… |  |  |
| GET|HEAD | api/v1/admin/payment-systems/payment-type-list | admin.payment_syst… |  |  |
| GET|HEAD | api/v1/admin/payment-systems/withdrawal-limit-period-list | admin.p… |  |  |
| GET|HEAD | api/v1/admin/payment-systems/withdrawal-rules-behavior-list/{withdrawalType} | admin.payment_systems.withdrawal_rules_behavior_list | Modules\Payment\Http\Controllers\Api\V1\Admin\PaymentSystemController@withdrawalRules… |  |
| GET|HEAD | api/v1/admin/payment-systems/withdrawal-type-list/{withdrawalType?} | admin.payment_systems.withdrawal_type_list | Modules\Payment\Http\Controllers\Api\V1\Admin\PaymentSystemController@withdrawalTypeL… |  |
| GET|HEAD | api/v1/admin/payment-systems/{payment_system} | admin.payment_syste… |  |  |
| POST | api/v1/admin/payment-systems/{payment_system} | admin.payment_syste… |  |  |
| POST | api/v1/admin/payment-systems/{payment_system}/custom | admin.paymen… |  |  |
| GET|HEAD | api/v1/admin/payment-systems/{payment_system}/readme | admin.paymen… |  |  |
| GET|HEAD | api/v1/admin/profile | admin.profile.show | Modules\User\Http\Contr… |  |
| GET|HEAD | api/v1/admin/settings/main | admin.settings.main.show | Modules\Set… |  |
| POST | api/v1/admin/settings/main | admin.settings.main.update | Modules\S… |  |
| GET|HEAD | api/v1/admin/settings/view | admin.settings.view.show | Modules\Set… |  |
| POST | api/v1/admin/settings/view | admin.settings.view.update | Modules\S… |  |
| GET|HEAD | api/v1/admin/shop/banners | admin.shop.banners.index | Modules\Shop… |  |
| POST | api/v1/admin/shop/banners | admin.shop.banners.store | Modules\Shop… |  |
| GET|HEAD | api/v1/admin/shop/banners/{id} | admin.shop.banners.show | Modules\… |  |
| PUT | api/v1/admin/shop/banners/{id} | admin.shop.banners.update | Module… |  |
| DELETE | api/v1/admin/shop/banners/{id} | admin.shop.banners.destroy | Modul… |  |
| GET|HEAD | api/v1/admin/shop/orders | admin.shop.orders.index | Modules\Shop\H… |  |
| POST | api/v1/admin/shop/orders | admin.shop.orders.store | Modules\Shop\H… |  |
| POST | api/v1/admin/shop/orders/batch-status-update | admin.shop.orders.ba… |  |  |
| GET|HEAD | api/v1/admin/shop/orders/bestsellers | admin.shop.orders.bestseller… |  |  |
| GET|HEAD | api/v1/admin/shop/orders/export | admin.shop.orders.export | Module… |  |
| GET|HEAD | api/v1/admin/shop/orders/statistic | admin.shop.orders.statistic | … |  |
| POST | api/v1/admin/shop/orders/users | admin.shop.orders.store_user | Mod… |  |
| GET|HEAD | api/v1/admin/shop/orders/{id} | admin.shop.orders.show | Modules\Sh… |  |
| PUT | api/v1/admin/shop/orders/{id} | admin.shop.orders.update | Modules\… |  |
| DELETE | api/v1/admin/shop/orders/{id} | admin.shop.orders.destroy | Modules… |  |
| GET|HEAD | api/v1/admin/shop/orders/{id}/statuses-history | admin.shop.orders.… |  |  |
| GET|HEAD | api/v1/admin/shop/product-categories | admin.shop.product_categorie… |  |  |
| POST | api/v1/admin/shop/product-categories | admin.shop.product_categorie… |  |  |
| GET|HEAD | api/v1/admin/shop/product-categories/export | admin.shop.product_ca… |  |  |
| GET|HEAD | api/v1/admin/shop/product-categories/tree | admin.shop.product_cate… |  |  |
| GET|HEAD | api/v1/admin/shop/product-categories/{id} | admin.shop.product_cate… |  |  |
| PUT | api/v1/admin/shop/product-categories/{id} | admin.shop.product_cate… |  |  |
| DELETE | api/v1/admin/shop/product-categories/{id} | admin.shop.product_cate… |  |  |
| GET|HEAD | api/v1/admin/shop/product-properties | admin.shop.product_propertie… |  |  |
| GET|HEAD | api/v1/admin/shop/product-special-statuses | admin.shop.product_spe… |  |  |
| POST | api/v1/admin/shop/product-special-statuses | admin.shop.product_spe… |  |  |
| GET|HEAD | api/v1/admin/shop/product-special-statuses/{id} | admin.shop.produc… |  |  |
| PUT | api/v1/admin/shop/product-special-statuses/{id} | admin.shop.produc… |  |  |
| DELETE | api/v1/admin/shop/product-special-statuses/{id} | admin.shop.produc… |  |  |
| GET|HEAD | api/v1/admin/shop/products | admin.shop.products.index | Modules\Sh… |  |
| POST | api/v1/admin/shop/products | admin.shop.products.store | Modules\Sh… |  |
| POST | api/v1/admin/shop/products/batch-special-statuses-update | admin.sh… |  |  |
| POST | api/v1/admin/shop/products/batch-status-update | admin.shop.product… |  |  |
| GET|HEAD | api/v1/admin/shop/products/export | admin.shop.products.export | Mo… |  |
| GET|HEAD | api/v1/admin/shop/products/{id} | admin.shop.products.show | Module… |  |
| PUT | api/v1/admin/shop/products/{id} | admin.shop.products.update | Modu… |  |
| DELETE | api/v1/admin/shop/products/{id} | admin.shop.products.destroy | Mod… |  |
| GET|HEAD | api/v1/admin/shop/products/{id}/related-products | admin.shop.produ… |  |  |
| GET|HEAD | api/v1/admin/shop/settings | admin.shop.settings.index | Modules\Sh… |  |
| PUT | api/v1/admin/shop/settings | admin.shop.settings.update | Modules\S… |  |
| GET|HEAD | api/v1/admin/telegram | admin.telegram.bot_info | Modules\Telegram\… |  |
| GET|HEAD | api/v1/admin/telegram/commands | admin.telegram.commands.index | Mo… |  |
| GET|HEAD | api/v1/admin/telegram/commands/{command} | admin.telegram.commands.… |  |  |
| PATCH | api/v1/admin/telegram/commands/{command} | admin.telegram.commands.… |  |  |
| POST | api/v1/admin/telegram/disable | admin.telegram.disable | Modules\Te… |  |
| POST | api/v1/admin/telegram/enable | admin.telegram.enable | Modules\Tele… |  |
| GET|HEAD | api/v1/admin/telegram/webhook | admin.telegram.webhook.show | Modul… |  |
| DELETE | api/v1/admin/telegram/webhook | admin.telegram.webhook.remove | Mod… |  |
| POST | api/v1/admin/translatable-locales/cache-clear | admin.translatable*… |  |  |
| POST | api/v1/admin/translations/cache-clear | admin.translations*cache_cl… |  |  |
| GET|HEAD | api/v1/admin/translator/queue/{id} | admin.translator.queue | Modul… |  |
| GET|HEAD | api/v1/admin/translator/translators | admin.translator.translators.… |  |  |
| PUT | api/v1/admin/translator/translators/{translator} | admin.translator… |  |  |
| POST | api/v1/admin/translator/translators/{translator}/translate | admin.… |  |  |
| GET|HEAD | api/v1/admin/user-management/roles | admin.user_management.roles.in… |  |  |
| GET|HEAD | api/v1/admin/user-management/sponsors | admin.user_management.spons… |  |  |
| GET|HEAD | api/v1/admin/user-management/sponsors/{id} | admin.user_management.… |  |  |
| GET|HEAD | api/v1/admin/user-management/user-registration-stats | admin.user_m… |  |  |
| GET|HEAD | api/v1/admin/user-management/users | admin.user_management.users.in… |  |  |
| POST | api/v1/admin/user-management/users | admin.user_management.users.st… |  |  |
| POST | api/v1/admin/user-management/users/confirm-user/{user} | admin.user… |  |  |
| GET|HEAD | api/v1/admin/user-management/users/export | admin.user_management.u… |  |  |
| POST | api/v1/admin/user-management/users/send-code-for-auth | admin.user*… |  |  |
| POST | api/v1/admin/user-management/users/{id}/block | admin.user*manageme… |  |  |
| POST | api/v1/admin/user-management/users/{id}/restore | admin.user_manage… |  |  |
| POST | api/v1/admin/user-management/users/{id}/unblock | admin.user_manage… |  |  |
| POST | api/v1/admin/user-management/users/{user} | admin.user_management.u… |  |  |
| GET|HEAD | api/v1/admin/user-management/users/{user} | admin.user_management.u… |  |  |
| DELETE | api/v1/admin/user-management/users/{user} | admin.user_management.u… |  |  |
| POST | api/v1/admin/user-management/users/{user}/auth | admin.user_managem… |  |  |
| GET|HEAD | api/v1/admin/users/{user}/accounts | admin.users.accounts.index | M… |  |
| GET|HEAD | api/v1/admin/verification | admin.verification.show | Modules\Verif… |  |
| PUT | api/v1/admin/verification | admin.verification.update | Modules\Ver… |  |
| GET|HEAD | api/v1/admin/verification/stages | admin.verification.stages.index |  |  |
| POST | api/v1/admin/verification/stages/update-set | admin.verification.st… |  |  |
| GET|HEAD | api/v1/admin/verification/user-document-items/download-zip | admin.… |  |  |
| GET|HEAD | api/v1/admin/verification/users | admin.verification.users.index | … |  |
| GET|HEAD | api/v1/admin/verification/users/export | admin.verification.users.e… |  |  |
| POST | api/v1/admin/verification/users/reject | admin.verification.users.r… |  |  |
| POST | api/v1/admin/verification/users/verify | admin.verification.users.v… |  |  |
| GET|HEAD | api/v1/admin/verification/users/{user} | admin.verification.users.s… |  |  |
| GET|HEAD | api/v1/admin/verification/users/{user}/document-items/download-zip | admin.verification.users.document_items.download_zip | Modules\Verification\Http\Controllers\Api\V1\Admin\UserDocumentItemController@downloadZ… |  |
| GET|HEAD | api/v1/admin/verification/users/{user}/document-items/{userDocumentItem}/download | admin.verification.users.document_items.download | Modules\Verification\Http\Controllers\Api\V1\Admin\UserDocumentItemCo… |  |
| POST | api/v1/admin/verification/users/{user}/reject | admin.verification.… |  |  |
| GET|HEAD | api/v1/admin/verification/users/{user}/stages | admin.verification.… |  |  |
| POST | api/v1/admin/verification/users/{user}/stages/{stage}/reject | admi… |  |  |
| POST | api/v1/admin/verification/users/{user}/stages/{stage}/verify | admi… |  |  |
| POST | api/v1/admin/verification/users/{user}/verify | admin.verification.… |  |  |
| GET|HEAD | api/v1/agreements/main | agreements.main | Modules\CustomConfig\Htt… |  |
| GET|HEAD | api/v1/auth-attempts | auth_attempts | Modules\User\Http\Controller… |  |
| GET|HEAD | api/v1/backups | backupslist | Modules\Core\Http\Controllers\Api\V1… |  |
| POST | api/v1/backups/dump | backupsdump | Modules\Core\Http\Controllers\A… |  |
| POST | api/v1/backups/restore | backupsrestore | Modules\Core\Http\Control… |  |
| GET|HEAD | api/v1/captcha | captcha.active | Modules\Captcha\Http\Controllers\… |  |
| GET|HEAD | api/v1/commands | commands.index | Modules\Core\Http\Controllers\Ap… |  |
| POST | api/v1/commands/{name} | commands.run | Modules\Core\Http\Controlle… |  |
| GET|HEAD | api/v1/company/departments | company.departments.index | Modules\Co… |  |
| GET|HEAD | api/v1/company/departments/{department} | company.departments.show |  |  |
| POST | api/v1/cramauth/challenge | cramauth.challenge | Modules\User\Http\… |  |
| POST | api/v1/cramauth/login | cramauth.login | Modules\User\Http\Controll… |  |
| POST | api/v1/cramauth/register | cramauth.register | Modules\User\Http\Co… |  |
| POST | api/v1/cramauth/{credentials}/revoke | cramauth.revoke | Modules\Us… |  |
| POST | api/v1/email/change-unverified | email.change_unverified | Modules\… |  |
| POST | api/v1/email/confirm-new | email.confirm_new | Modules\User\Http\Co… |  |
| POST | api/v1/email/confirm-old | email.confirm_old | Modules\User\Http\Co… |  |
| POST | api/v1/email/send-verification | email.send_verification | Modules\… |  |
| POST | api/v1/email/verify | email.verify | Modules\User\Http\Controllers\… |  |
| GET|HEAD | api/v1/estate/acts | estate.acts.index | Modules\Estate\Http\Contro… |  |
| POST | api/v1/estate/acts | estate.acts.store | Modules\Estate\Http\Contro… |  |
| GET|HEAD | api/v1/estate/acts/statuses | estate.acts.statuses | Modules\Estate… |  |
| GET|HEAD | api/v1/estate/acts/types | estate.acts.types | Modules\Estate\Http\… |  |
| GET|HEAD | api/v1/estate/acts/{id} | estate.acts.show | Modules\Estate\Http\Co… |  |
| POST | api/v1/estate/acts/{id} | estate.acts.update | Modules\Estate\Http\… |  |
| POST | api/v1/estate/agencies | estate.agencies.store | Modules\Estate\Htt… |  |
| DELETE | api/v1/estate/agencies/delete_role/{id} | estate.agencies.delete_ro… |  |  |
| GET|HEAD | api/v1/estate/agencies/divisions | estate.agencies.divisions.index |  |  |
| POST | api/v1/estate/agencies/divisions | estate.agencies.divisions.store |  |  |
| GET|HEAD | api/v1/estate/agencies/divisions/{id} | estate.agencies.divisions.s… |  |  |
| POST | api/v1/estate/agencies/divisions/{id} | estate.agencies.divisions.u… |  |  |
| DELETE | api/v1/estate/agencies/divisions/{id} | estate.agencies.divisions.d… |  |  |
| GET|HEAD | api/v1/estate/agencies/legal_entities | estate.agencies.legal_entit… |  |  |
| POST | api/v1/estate/agencies/legal_entities | estate.agencies.legal_entit… |  |  |
| GET|HEAD | api/v1/estate/agencies/legal_entities/digital_signature_operator_list | estate.agencies.legal_entities.digital_signature_operator_list | Modules\Estate\Http\Controllers\Api\V1\AgencyLegalEntityController@digital_signature_operator… |  |
| GET|HEAD | api/v1/estate/agencies/legal_entities/has_nds_list | estate.agencie… |  |  |
| GET|HEAD | api/v1/estate/agencies/legal_entities/types | estate.agencies.legal… |  |  |
| GET|HEAD | api/v1/estate/agencies/legal_entities/{id} | estate.agencies.legal*… |  |  |
| POST | api/v1/estate/agencies/legal*entities/{id} | estate.agencies.legal*… |  |  |
| GET|HEAD | api/v1/estate/agencies/permissions | estate.agencies.permissions | … |  |
| GET|HEAD | api/v1/estate/agencies/providers | estate.agencies.providers.index |  |  |
| POST | api/v1/estate/agencies/providers/change | estate.agencies.providers… |  |  |
| GET|HEAD | api/v1/estate/agencies/roles | estate.agencies.roles | Modules\Esta… |  |
| POST | api/v1/estate/agencies/send*for_moderation | estate.agencies.send_f… |  |  |
| POST | api/v1/estate/agencies/staff | estate.agencies.staff.store | Module… |  |
| GET|HEAD | api/v1/estate/agencies/staff/current | estate.agencies.staff.curren… |  |  |
| POST | api/v1/estate/agencies/staff/reinstate/{id} | estate.agencies.staff… |  |  |
| GET|HEAD | api/v1/estate/agencies/staff/roles/{id} | estate.agencies.staff.rol… |  |  |
| POST | api/v1/estate/agencies/staff/update_roles/{id} | estate.agencies.st… |  |  |
| POST | api/v1/estate/agencies/staff/{id} | estate.agencies.staff.update | … |  |
| GET|HEAD | api/v1/estate/agencies/staff/{id} | estate.agencies.staff.show | Mo… |  |
| DELETE | api/v1/estate/agencies/staff/{id} | estate.agencies.staff.destroy |  |  |
| POST | api/v1/estate/agencies/store_role | estate.agencies.store_role | Mo… |  |
| POST | api/v1/estate/agencies/update_access | estate.agencies.update_acces… |  |  |
| POST | api/v1/estate/agencies/update_role/{id} | estate.agencies.update_ro… |  |  |
| POST | api/v1/estate/agencies/update_role_permissions/{id} | estate.agenci… |  |  |
| GET|HEAD | api/v1/estate/agencies/{id} | estate.agencies.show | Modules\Estate… |  |
| POST | api/v1/estate/agencies/{id} | estate.agencies.update | Modules\Esta… |  |
| GET|HEAD | api/v1/estate/aggregator_legal_entities | estate.aggregator_legal_e… |  |  |
| GET|HEAD | api/v1/estate/apartment_statuses | estate.apartment_statuses.index |  |  |
| GET|HEAD | api/v1/estate/apartment_statuses/{id} | estate.apartment_statuses.s… |  |  |
| GET|HEAD | api/v1/estate/apartment_types | estate.apartment_types.index | Modu… |  |
| GET|HEAD | api/v1/estate/apartment_types/fast | estate.apartment_types.fast | … |  |
| GET|HEAD | api/v1/estate/apartment_types/{id} | estate.apartment_types.show | … |  |
| GET|HEAD | api/v1/estate/apartments | estate.apartments.index | Modules\Estate… |  |
| GET|HEAD | api/v1/estate/apartments/fast | estate.apartments.fast | Modules\Es… |  |
| GET|HEAD | api/v1/estate/apartments/{id} | estate.apartments.show | Modules\Es… |  |
| GET|HEAD | api/v1/estate/banks | estate.banks.index | Modules\Estate\Http\Cont… |  |
| GET|HEAD | api/v1/estate/banks/{id} | estate.banks.show | Modules\Estate\Http\… |  |
| GET|HEAD | api/v1/estate/clients | estate.clients.index | Modules\Estate\Http\… |  |
| POST | api/v1/estate/clients | estate.clients.store | Modules\Estate\Http\… |  |
| GET|HEAD | api/v1/estate/clients/{id} | estate.clients.show | Modules\Estate\H… |  |
| POST | api/v1/estate/clients/{id} | estate.clients.update | Modules\Estate… |  |
| DELETE | api/v1/estate/clients/{id} | estate.clients.destroy | Modules\Estat… |  |
| GET|HEAD | api/v1/estate/clients/{id}/deals | estate.clients.indexDeals | Modu… |  |
| GET|HEAD | api/v1/estate/clients/{id}/history | estate.clients.indexHistory | … |  |
| GET|HEAD | api/v1/estate/deal_types | estate.deal_types.index | Modules\Estate… |  |
| GET|HEAD | api/v1/estate/deals | estate.deals.index | Modules\Estate\Http\Cont… |  |
| POST | api/v1/estate/deals | estate.deals.store | Modules\Estate\Http\Cont… |  |
| POST | api/v1/estate/deals/change_status/{id} | estate.deals.change_status… |  |  |
| GET|HEAD | api/v1/estate/deals/status_history/{id} | estate.deals.status_histo… |  |  |
| GET|HEAD | api/v1/estate/deals/statuses | estate.deals.statuses | Modules\Esta… |  |
| GET|HEAD | api/v1/estate/deals/{id} | estate.deals.show | Modules\Estate\Http\… |  |
| POST | api/v1/estate/deals/{id} | estate.deals.update | Modules\Estate\Htt… |  |
| DELETE | api/v1/estate/deals/{id} | estate.deals.destroy | Modules\Estate\Ht… |  |
| GET|HEAD | api/v1/estate/decoration_types | estate.decoration_types.index | Mo… |  |
| GET|HEAD | api/v1/estate/decoration_types/{id} | estate.decoration_types.show |  |  |
| GET|HEAD | api/v1/estate/districts | estate.districts.index | Modules\Estate\H… |  |
| GET|HEAD | api/v1/estate/districts/list | estate.districts.list | Modules\Esta… |  |
| GET|HEAD | api/v1/estate/districts/{id} | estate.districts.show | Modules\Esta… |  |
| GET|HEAD | api/v1/estate/elevator_types | estate.elevator_types.index | Module… |  |
| GET|HEAD | api/v1/estate/elevator_types/{id} | estate.elevator_types.show | Mo… |  |
| GET|HEAD | api/v1/estate/estate_object_types | estate.estate_object_types.inde… |  |  |
| GET|HEAD | api/v1/estate/estate_payment_types | estate.estate_payment_types.in… |  |  |
| GET|HEAD | api/v1/estate/estates/{id} | estate.estates.show | Modules\Estate\H… |  |
| GET|HEAD | api/v1/estate/hc_classes | estate.hc_classes.index | Modules\Estate… |  |
| GET|HEAD | api/v1/estate/hc_classes/{id} | estate.hc_classes.show | Modules\Es… |  |
| GET|HEAD | api/v1/estate/hc_types | estate.hc_types.index | Modules\Estate\Htt… |  |
| GET|HEAD | api/v1/estate/hc_types/{id} | estate.hc_types.show | Modules\Estate… |  |
| GET|HEAD | api/v1/estate/housing_complexes | estate.housing_complexes.index | … |  |
| GET|HEAD | api/v1/estate/housing_complexes/commercial | estate.housing_complex… |  |  |
| GET|HEAD | api/v1/estate/housing_complexes/delivery-quarters | estate.housing*… |  |  |
| GET|HEAD | api/v1/estate/housing*complexes/for_map | estate.housing_complexes.… |  |  |
| GET|HEAD | api/v1/estate/housing_complexes/listing_apartments | estate.housing… |  |  |
| GET|HEAD | api/v1/estate/housing_complexes/new | estate.housing_complexes.new |  |  |
| GET|HEAD | api/v1/estate/housing_complexes/show-apartments-data/{id} | estate.… |  |  |
| GET|HEAD | api/v1/estate/housing_complexes/{id} | estate.housing_complexes.sho… |  |  |
| GET|HEAD | api/v1/estate/leads/{uuid} | estate.leads.show | Modules\Estate\Htt… |  |
| GET|HEAD | api/v1/estate/metros | estate.metros.index | Modules\Estate\Http\Co… |  |
| POST | api/v1/estate/object_info | estate.object_info | Modules\Estate\Htt… |  |
| GET|HEAD | api/v1/estate/parking_locations | estate.parking_locations.index | … |  |
| GET|HEAD | api/v1/estate/parking_locations/{id} | estate.parking_locations.sho… |  |  |
| GET|HEAD | api/v1/estate/parking_types | estate.parking_types.index | Modules\… |  |
| GET|HEAD | api/v1/estate/parking_types/{id} | estate.parking_types.show | Modu… |  |
| GET|HEAD | api/v1/estate/payments | estate.payments.index | Modules\Estate\Htt… |  |
| GET|HEAD | api/v1/estate/providers | estate.providers.index | Modules\Estate\H… |  |
| GET|HEAD | api/v1/estate/providers/{id} | estate.providers.show | Modules\Esta… |  |
| GET|HEAD | api/v1/estate/regulation_tariff_cards | estate.regulation_tariff_ca… |  |  |
| GET|HEAD | api/v1/estate/regulation_tariff_cards/{id} | estate.regulation_tari… |  |  |
| GET|HEAD | api/v1/estate/regulations | estate.regulations.index | Modules\Esta… |  |
| GET|HEAD | api/v1/estate/regulations/statuses | estate.regulations.statuses | … |  |
| GET|HEAD | api/v1/estate/regulations/{id} | estate.regulations.show | Modules\… |  |
| GET|HEAD | api/v1/estate/room_types | estate.room_types.index | Modules\Estate… |  |
| GET|HEAD | api/v1/estate/room_types/{id} | estate.room_types.show | Modules\Es… |  |
| POST | api/v1/estate/selections | estate.selections.store | Modules\Estate… |  |
| GET|HEAD | api/v1/estate/selections/client/{id} | estate.selections.show_by_cl… |  |  |
| PUT | api/v1/estate/selections/presentation/hide/{selection_uuid} | chang… |  |  |
| GET|HEAD | api/v1/estate/selections/presentation/{selection_uuid} | show_prese… |  |  |
| DELETE | api/v1/estate/selections/{id} | estate.selections.destroy | Modules… |  |
| DELETE | api/v1/estate/selections/{selection_id}/apartment/{apartment_id} | … |  |  |
| GET|HEAD | api/v1/estate/wishlist/apartments | estate.wishlist.apartments.inde… |  |  |
| POST | api/v1/estate/wishlist/apartments/add/{item} | estate.wishlist.apar… |  |  |
| GET|HEAD | api/v1/estate/wishlist/apartments/list | estate.wishlist.apartments… |  |  |
| POST | api/v1/estate/wishlist/apartments/remove | estate.wishlist.apartmen… |  |  |
| GET|HEAD | api/v1/estate/wishlist/housing_complexes | estate.wishlist.housing*… |  |  |
| POST | api/v1/estate/wishlist/housing*complexes/add/{item} | estate.wishli… |  |  |
| GET|HEAD | api/v1/estate/wishlist/housing_complexes/list | estate.wishlist.hou… |  |  |
| POST | api/v1/estate/wishlist/housing_complexes/remove | estate.wishlist.h… |  |  |
| GET|HEAD | api/v1/export/download/{id}/{token} | export.download | Modules\Cor… |  |
| GET|HEAD | api/v1/export/queue/{id} | export.queue | Modules\Core\Http\Control… |  |
| GET|HEAD | api/v1/faq/categories | faq.categories.index | Modules\Faq\Http\Con… |  |
| GET|HEAD | api/v1/faq/categories/{category_id} | faq.categories.show | Modules… |  |
| GET|HEAD | api/v1/faq/questions | faq.questions.index | Modules\Faq\Http\Contr… |  |
| GET|HEAD | api/v1/faq/questions/{question_id} | faq.questions.show | Modules\F… |  |
| POST | api/v1/feedback/queries | feedback.queries.store | Modules\Feedback… |  |
| GET|HEAD | api/v1/feedback/queries/can-query | feedback.queries.can_query | Mo… |  |
| GET|HEAD | api/v1/feedback/queries/form-text | feedback.queries.form_text | Mo… |  |
| GET|HEAD | api/v1/feedback/queries/support | feedback.queries.support | Module… |  |
| GET|HEAD | api/v1/feedback/query-themes | feedback.query_themes.index | Module… |  |
| POST | api/v1/feedback/reviews/{feedbackReview} | feedback.reviews.reply |  |  |
| PATCH | api/v1/feedback/reviews/{feedbackReview} | feedback.reviews.update |  |  |
| DELETE | api/v1/feedback/reviews/{feedbackReview} | feedback.reviews.destroy… |  |  |
| POST | api/v1/feedback/reviews/{feedbackReview}/votes | feedback.reviews.v… |  |  |
| GET|HEAD | api/v1/feedback/reviews/{type}/{id} | feedback.reviews.index | Modu… |  |
| POST | api/v1/feedback/reviews/{type}/{id} | feedback.reviews.store | Modu… |  |
| GET|HEAD | api/v1/geonames/cities | geonames.cities | Modules\CustomConfig\Htt… |  |
| GET|HEAD | api/v1/geonames/cities-of-country/{countryCode} | geonames.cities_o… |  |  |
| GET|HEAD | api/v1/geonames/cities-of-state/{countryCode}/{admin1} | geonames.c… |  |  |
| GET|HEAD | api/v1/geonames/countries | geonames.countries | Modules\Core\Http\… |  |
| GET|HEAD | api/v1/geonames/country-by-ip | geonames.country_by_ip | Modules\Co… |  |
| GET|HEAD | api/v1/geonames/states | geonames.states | Modules\Core\Http\Contro… |  |
| GET|HEAD | api/v1/geonames/states-of-country/{countryCode} | geonames.states_o… |  |  |
| GET|HEAD | api/v1/geonames/{id} | geonames.show | Modules\Core\Http\Controller… |  |
| POST | api/v1/login | login | Modules\User\Http\Controllers\Api\V1\AuthCon… |  |
| POST | api/v1/logout | logout | Modules\User\Http\Controllers\Api\V1\AuthC… |  |
| POST | api/v1/mailgun-callback | mailgun_callback | Modules\Notifications\… |  |
| GET|HEAD | api/v1/news | news.index | Modules\CustomConfig\Http\Controllers\Ap… |  |
| GET|HEAD | api/v1/news/categories | news.categories.index | Modules\News\Http\… |  |
| GET|HEAD | api/v1/news/categories/{id} | news.categories.show | Modules\News\H… |  |
| GET|HEAD | api/v1/news/categories/{url} | news.categories.show_by_url | Module… |  |
| GET|HEAD | api/v1/news/{id} | news.show | Modules\CustomConfig\Http\Controller… |  |
| GET|HEAD | api/v1/news/{url} | news.show_by_url | Modules\CustomConfig\Http\Co… |  |
| GET|HEAD | api/v1/notifications | notifications.index | Modules\Estate\Http\Co… |  |
| POST | api/v1/notifications/clear_unread | notifications.clear_unread | Mo… |  |
| GET|HEAD | api/v1/notifications/unread_count | notifications.unread_count | Mo… |  |
| POST | api/v1/password/recover | password.recover | Modules\User\Http\Cont… |  |
| POST | api/v1/password/reset | password.reset | Modules\User\Http\Controll… |  |
| GET|HEAD | api/v1/password/reset-token/{email}/{token} | password.reset_token |  |  |
| GET|HEAD | api/v1/payment-systems | payment_systems.index | Modules\Payment\Ht… |  |
| POST | api/v1/payment-systems/calculate-amount | payment_systems.calculate… |  |  |
| GET|HEAD | api/v1/payment-systems/payment-form/{document} | payment_systems.pa… |  |  |
| PATCH | api/v1/payment-systems/payment-form/{document} | payment_systems.pa… |  |  |
| POST | api/v1/payment-systems/replenishment | payment_systems.replenishmen… |  |  |
| POST | api/v1/payment-systems/user-account | payment_systems.user_account |  |  |
| POST | api/v1/payment-systems/withdrawal | payment_systems.withdrawal | Mo… |  |
| POST | api/v1/personal-access-tokens | .............. |  |  |
| GET|HEAD | api/v1/presentation/apartments/{modelUuid}/{agentUuid} | presentati… |  |  |
| GET|HEAD | api/v1/presentation/estates/{item} | presentation.estate_presentati… |  |  |
| GET|HEAD | api/v1/presentation/housing_complexes/{hcUuid}/{agentUuid} | presen… |  |  |
| POST | api/v1/register | register | Modules\User\Http\Controllers\Api\V1\R… |  |
| POST | api/v1/register/check_email_code | register.check_email_code | Modu… |  |
| POST | api/v1/register/check_phone_code | register.check_phone_code | Modu… |  |
| POST | api/v1/register/send_email_code | register.send_email_code | Module… |  |
| POST | api/v1/register/send_phone_code | register.send_phone_code | Module… |  |
| GET|HEAD | api/v1/scopes | ....................................... |  |  |
| GET|HEAD | api/v1/settings/date | settings.date | Modules\Settings\Http\Contro… |  |
| GET|HEAD | api/v1/shop/banners | shop.banners.index | Modules\Shop\Http\Contro… |  |
| GET|HEAD | api/v1/shop/banners/{id} | shop.banners.show | Modules\Shop\Http\Co… |  |
| POST | api/v1/shop/carts | shop.carts.store | Modules\Shop\Http\Controller… |  |
| POST | api/v1/shop/carts/{cart}/checkout | shop.carts.checkout | Modules\S… |  |
| GET|HEAD | api/v1/shop/carts/{cart}/user-account-list | shop.carts.user_accoun… |  |  |
| GET|HEAD | api/v1/shop/carts/{id} | shop.carts.show | Modules\Shop\Http\Contro… |  |
| DELETE | api/v1/shop/carts/{id} | shop.carts.destroy | Modules\Shop\Http\Con… |  |
| POST | api/v1/shop/carts/{id}/add-product | shop.carts.add_product | Modul… |  |
| DELETE | api/v1/shop/carts/{id}/clear | shop.carts.clear | Modules\Shop\Http… |  |
| DELETE | api/v1/shop/carts/{id}/delete-product | shop.carts.delete_product |  |  |
| DELETE | api/v1/shop/carts/{id}/remove-product | shop.carts.remove_product |  |  |
| POST | api/v1/shop/carts/{id}/set-product | shop.carts.set_product | Modul… |  |
| GET|HEAD | api/v1/shop/orders | shop.orders.index | Modules\Shop\Http\Controll… |  |
| GET|HEAD | api/v1/shop/orders/export | shop.orders.export | Modules\Shop\Http\… |  |
| GET|HEAD | api/v1/shop/orders/{id} | shop.orders.show | Modules\Shop\Http\Cont… |  |
| GET|HEAD | api/v1/shop/orders/{id}/statuses-history | shop.orders.statuses_his… |  |  |
| POST | api/v1/shop/orders/{order}/repeat | shop.orders.repeat | Modules\Sh… |  |
| GET|HEAD | api/v1/shop/product-categories | shop.product_categories.index | Mo… |  |
| GET|HEAD | api/v1/shop/product-categories/{id} | shop.product_categories.show |  |  |
| GET|HEAD | api/v1/shop/product-categories/{url} | shop.product_categories.show… |  |  |
| GET|HEAD | api/v1/shop/product-properties | shop.product_properties.index | Mo… |  |
| GET|HEAD | api/v1/shop/products | shop.products.index | Modules\Shop\Http\Cont… |  |
| GET|HEAD | api/v1/shop/products/hot-titles | shop.products.hot_titles | Module… |  |
| GET|HEAD | api/v1/shop/products/popular | shop.products.popular | Modules\Shop… |  |
| GET|HEAD | api/v1/shop/products/{id} | shop.products.show | Modules\Shop\Http\… |  |
| GET|HEAD | api/v1/shop/products/{id}/related-products | shop.products.related*… |  |  |
| POST | api/v1/shop/wishlist/add-to-cart | shop.wishlist.add*to_cart | Modu… |  |
| GET|HEAD | api/v1/shop/wishlist/product-list | shop.wishlist.product_list | Mo… |  |
| GET|HEAD | api/v1/shop/wishlist/products | shop.wishlist.products | Modules\Sh… |  |
| POST | api/v1/shop/wishlist/products/{product} | shop.wishlist.add_product… |  |  |
| DELETE | api/v1/shop/wishlist/products/{product} | shop.wishlist.remove_prod… |  |  |
| POST | api/v1/shop/wishlist/remove-products | shop.wishlist.remove_product… |  |  |
| GET|HEAD | api/v1/site/register-data | site.registerData | Modules\CustomConfi… |  |
| POST | api/v1/site/sync-reset-password | site.syncResetPassword | Modules\… |  |
| GET|HEAD | api/v1/sponsor-details/{username} | site.showSponsorDetail | Module… |  |
| GET|HEAD | api/v1/sponsors/{username} | sponsors.show | Modules\User\Http\Cont… |  |
| POST | api/v1/sso/agencies | sso.agencies.store | Modules\Estate\Http\Cont… |  |
| POST | api/v1/sso/agencies/simple | sso.agencies.store_simple | Modules\Es… |  |
| PUT | api/v1/sso/agencies/update | sso.agencies.update_agency | Modules\E… |  |
| POST | api/v1/sso/login | sso.login | Modules\Estate\Http\Controllers\Sso\… |  |
| POST | api/v1/sso/register | sso.register.register | Modules\Estate\Http\C… |  |
| POST | api/v1/sso/register/simple | sso.register.register_simple | Modules… |  |
| PUT | api/v1/sso/register/update | sso.register.update_agent | Modules\Es… |  |
| POST | api/v1/sync/estate/agencies | sync.estate.agencies.store | Modules\… |  |
| POST | api/v1/sync/estate/agencies/legal_entities | sync.estate.agencies.l… |  |  |
| GET|HEAD | api/v1/sync/estate/agencies/legal_entities/{uuid} | sync.estate.age… |  |  |
| PUT | api/v1/sync/estate/agencies/legal_entities/{uuid} | sync.estate.age… |  |  |
| DELETE | api/v1/sync/estate/agencies/legal_entities/{uuid} | sync.estate.age… |  |  |
| GET|HEAD | api/v1/sync/estate/agencies/{uuid} | sync.estate.agencies.show | Mo… |  |
| PUT | api/v1/sync/estate/agencies/{uuid} | sync.estate.agencies.update | … |  |
| DELETE | api/v1/sync/estate/agencies/{uuid} | sync.estate.agencies.destroy |  |  |
| POST | api/v1/sync/estate/apartment_balconies | sync.estate.apartment_balc… |  |  |
| GET|HEAD | api/v1/sync/estate/apartment_balconies/{uuid} | sync.estate.apartme… |  |  |
| PUT | api/v1/sync/estate/apartment_balconies/{uuid} | sync.estate.apartme… |  |  |
| DELETE | api/v1/sync/estate/apartment_balconies/{uuid} | sync.estate.apartme… |  |  |
| POST | api/v1/sync/estate/apartment_types | sync.estate.apartment_types.st… |  |  |
| GET|HEAD | api/v1/sync/estate/apartment_types/{uuid} | sync.estate.apartment_t… |  |  |
| PUT | api/v1/sync/estate/apartment_types/{uuid} | sync.estate.apartment_t… |  |  |
| DELETE | api/v1/sync/estate/apartment_types/{uuid} | sync.estate.apartment_t… |  |  |
| POST | api/v1/sync/estate/apartments | sync.estate.apartments.store | Modu… |  |
| GET|HEAD | api/v1/sync/estate/apartments/{uuid} | sync.estate.apartments.show |  |  |
| PUT | api/v1/sync/estate/apartments/{uuid} | sync.estate.apartments.updat… |  |  |
| DELETE | api/v1/sync/estate/apartments/{uuid} | sync.estate.apartments.destr… |  |  |
| POST | api/v1/sync/estate/calculation_indicators | sync.estate.calculation… |  |  |
| GET|HEAD | api/v1/sync/estate/calculation_indicators/{uuid} | sync.estate.calc… |  |  |
| PUT | api/v1/sync/estate/calculation_indicators/{uuid} | sync.estate.calc… |  |  |
| DELETE | api/v1/sync/estate/calculation_indicators/{uuid} | sync.estate.calc… |  |  |
| POST | api/v1/sync/estate/calculation_methods | sync.estate.calculation_me… |  |  |
| GET|HEAD | api/v1/sync/estate/calculation_methods/{uuid} | sync.estate.calcula… |  |  |
| PUT | api/v1/sync/estate/calculation_methods/{uuid} | sync.estate.calcula… |  |  |
| DELETE | api/v1/sync/estate/calculation_methods/{uuid} | sync.estate.calcula… |  |  |
| POST | api/v1/sync/estate/calculation_months | sync.estate.calculation_mon… |  |  |
| GET|HEAD | api/v1/sync/estate/calculation_months/{uuid} | sync.estate.calculat… |  |  |
| PUT | api/v1/sync/estate/calculation_months/{uuid} | sync.estate.calculat… |  |  |
| DELETE | api/v1/sync/estate/calculation_months/{uuid} | sync.estate.calculat… |  |  |
| POST | api/v1/sync/estate/cities | sync.estate.cities.store | Modules\Esta… |  |
| GET|HEAD | api/v1/sync/estate/cities/{uuid} | sync.estate.cities.show | Module… |  |
| PUT | api/v1/sync/estate/cities/{uuid} | sync.estate.cities.update | Modu… |  |
| DELETE | api/v1/sync/estate/cities/{uuid} | sync.estate.cities.destroy | Mod… |  |
| POST | api/v1/sync/estate/clients | sync.estate.clients.store | Modules\Es… |  |
| GET|HEAD | api/v1/sync/estate/clients/{uuid} | sync.estate.clients.show | Modu… |  |
| PUT | api/v1/sync/estate/clients/{uuid} | sync.estate.clients.update | Mo… |  |
| DELETE | api/v1/sync/estate/clients/{uuid} | sync.estate.clients.destroy | M… |  |
| POST | api/v1/sync/estate/countries | sync.estate.countries.store | Module… |  |
| GET|HEAD | api/v1/sync/estate/countries/{uuid} | sync.estate.countries.show | … |  |
| PUT | api/v1/sync/estate/countries/{uuid} | sync.estate.countries.update |  |  |
| DELETE | api/v1/sync/estate/countries/{uuid} | sync.estate.countries.destroy… |  |  |
| POST | api/v1/sync/estate/deal_types | sync.estate.deal_types.store | Modu… |  |
| GET|HEAD | api/v1/sync/estate/deal_types/{uuid} | sync.estate.deal_types.show |  |  |
| PUT | api/v1/sync/estate/deal_types/{uuid} | sync.estate.deal_types.updat… |  |  |
| DELETE | api/v1/sync/estate/deal_types/{uuid} | sync.estate.deal_types.destr… |  |  |
| POST | api/v1/sync/estate/deals | sync.estate.deals.store | Modules\Estate… |  |
| GET|HEAD | api/v1/sync/estate/deals/{uuid} | sync.estate.deals.show | Modules\… |  |
| PUT | api/v1/sync/estate/deals/{uuid} | sync.estate.deals.update | Module… |  |
| DELETE | api/v1/sync/estate/deals/{uuid} | sync.estate.deals.destroy | Modul… |  |
| POST | api/v1/sync/estate/decoration_types | sync.estate.decoration_types.… |  |  |
| GET|HEAD | api/v1/sync/estate/decoration_types/{uuid} | sync.estate.decoration… |  |  |
| PUT | api/v1/sync/estate/decoration_types/{uuid} | sync.estate.decoration… |  |  |
| DELETE | api/v1/sync/estate/decoration_types/{uuid} | sync.estate.decoration… |  |  |
| POST | api/v1/sync/estate/developers | sync.estate.developers.store | Modu… |  |
| GET|HEAD | api/v1/sync/estate/developers/{uuid} | sync.estate.developers.show |  |  |
| PUT | api/v1/sync/estate/developers/{uuid} | sync.estate.developers.updat… |  |  |
| DELETE | api/v1/sync/estate/developers/{uuid} | sync.estate.developers.destr… |  |  |
| POST | api/v1/sync/estate/districts | sync.estate.districts.store | Module… |  |
| GET|HEAD | api/v1/sync/estate/districts/{uuid} | sync.estate.districts.show | … |  |
| PUT | api/v1/sync/estate/districts/{uuid} | sync.estate.districts.update |  |  |
| DELETE | api/v1/sync/estate/districts/{uuid} | sync.estate.districts.destroy… |  |  |
| POST | api/v1/sync/estate/elevator_types | sync.estate.elevator_types.stor… |  |  |
| GET|HEAD | api/v1/sync/estate/elevator_types/{uuid} | sync.estate.elevator_typ… |  |  |
| PUT | api/v1/sync/estate/elevator_types/{uuid} | sync.estate.elevator_typ… |  |  |
| DELETE | api/v1/sync/estate/elevator_types/{uuid} | sync.estate.elevator_typ… |  |  |
| POST | api/v1/sync/estate/entrances | sync.estate.entrances.store | Module… |  |
| GET|HEAD | api/v1/sync/estate/entrances/{uuid} | sync.estate.entrances.show | … |  |
| PUT | api/v1/sync/estate/entrances/{uuid} | sync.estate.entrances.update |  |  |
| DELETE | api/v1/sync/estate/entrances/{uuid} | sync.estate.entrances.destroy… |  |  |
| POST | api/v1/sync/estate/estate_payment_types | sync.estate.estate_paymen… |  |  |
| GET|HEAD | api/v1/sync/estate/estate_payment_types/{uuid} | sync.estate.estate… |  |  |
| PUT | api/v1/sync/estate/estate_payment_types/{uuid} | sync.estate.estate… |  |  |
| DELETE | api/v1/sync/estate/estate_payment_types/{uuid} | sync.estate.estate… |  |  |
| POST | api/v1/sync/estate/estate_types | sync.estate.estate_types.store | … |  |
| GET|HEAD | api/v1/sync/estate/estate_types/{uuid} | sync.estate.estate_types.s… |  |  |
| PUT | api/v1/sync/estate/estate_types/{uuid} | sync.estate.estate_types.u… |  |  |
| DELETE | api/v1/sync/estate/estate_types/{uuid} | sync.estate.estate_types.d… |  |  |
| POST | api/v1/sync/estate/estates | sync.estate.estates.store | Modules\Es… |  |
| GET|HEAD | api/v1/sync/estate/estates/{uuid} | sync.estate.estates.show | Modu… |  |
| PUT | api/v1/sync/estate/estates/{uuid} | sync.estate.estates.update | Mo… |  |
| DELETE | api/v1/sync/estate/estates/{uuid} | sync.estate.estates.destroy | M… |  |
| POST | api/v1/sync/estate/facade_types | sync.estate.facade_types.store | … |  |
| GET|HEAD | api/v1/sync/estate/facade_types/{uuid} | sync.estate.facade_types.s… |  |  |
| PUT | api/v1/sync/estate/facade_types/{uuid} | sync.estate.facade_types.u… |  |  |
| DELETE | api/v1/sync/estate/facade_types/{uuid} | sync.estate.facade_types.d… |  |  |
| POST | api/v1/sync/estate/hc_classes | sync.estate.hc_classes.store | Modu… |  |
| GET|HEAD | api/v1/sync/estate/hc_classes/{uuid} | sync.estate.hc_classes.show |  |  |
| PUT | api/v1/sync/estate/hc_classes/{uuid} | sync.estate.hc_classes.updat… |  |  |
| DELETE | api/v1/sync/estate/hc_classes/{uuid} | sync.estate.hc_classes.destr… |  |  |
| POST | api/v1/sync/estate/hc_types | sync.estate.hc_types.store | Modules\… |  |
| GET|HEAD | api/v1/sync/estate/hc_types/{uuid} | sync.estate.hc_types.show | Mo… |  |
| PUT | api/v1/sync/estate/hc_types/{uuid} | sync.estate.hc_types.update | … |  |
| DELETE | api/v1/sync/estate/hc_types/{uuid} | sync.estate.hc_types.destroy |  |  |
| POST | api/v1/sync/estate/housing_complexes | sync.estate.housing_complexe… |  |  |
| GET|HEAD | api/v1/sync/estate/housing_complexes/{uuid} | sync.estate.housing_c… |  |  |
| PUT | api/v1/sync/estate/housing_complexes/{uuid} | sync.estate.housing_c… |  |  |
| DELETE | api/v1/sync/estate/housing_complexes/{uuid} | sync.estate.housing_c… |  |  |
| POST | api/v1/sync/estate/leads | sync.estate.leads.store | Modules\Estate… |  |
| POST | api/v1/sync/estate/metro_lines | sync.estate.metro_lines.store | Mo… |  |
| GET|HEAD | api/v1/sync/estate/metro_lines/{uuid} | sync.estate.metro_lines.sho… |  |  |
| PUT | api/v1/sync/estate/metro_lines/{uuid} | sync.estate.metro_lines.upd… |  |  |
| DELETE | api/v1/sync/estate/metro_lines/{uuid} | sync.estate.metro_lines.des… |  |  |
| POST | api/v1/sync/estate/metros | sync.estate.metros.store | Modules\Esta… |  |
| GET|HEAD | api/v1/sync/estate/metros/{uuid} | sync.estate.metros.show | Module… |  |
| PUT | api/v1/sync/estate/metros/{uuid} | sync.estate.metros.update | Modu… |  |
| DELETE | api/v1/sync/estate/metros/{uuid} | sync.estate.metros.destroy | Mod… |  |
| POST | api/v1/sync/estate/parking_types | sync.estate.parking_types.store |  |  |
| GET|HEAD | api/v1/sync/estate/parking_types/{uuid} | sync.estate.parking_types… |  |  |
| PUT | api/v1/sync/estate/parking_types/{uuid} | sync.estate.parking_types… |  |  |
| DELETE | api/v1/sync/estate/parking_types/{uuid} | sync.estate.parking_types… |  |  |
| POST | api/v1/sync/estate/providers | sync.estate.providers.store | Module… |  |
| GET|HEAD | api/v1/sync/estate/providers/{uuid} | sync.estate.providers.show | … |  |
| PUT | api/v1/sync/estate/providers/{uuid} | sync.estate.providers.update |  |  |
| DELETE | api/v1/sync/estate/providers/{uuid} | sync.estate.providers.destroy… |  |  |
| POST | api/v1/sync/estate/regions | sync.estate.regions.store | Modules\Es… |  |
| GET|HEAD | api/v1/sync/estate/regions/{uuid} | sync.estate.regions.show | Modu… |  |
| PUT | api/v1/sync/estate/regions/{uuid} | sync.estate.regions.update | Mo… |  |
| DELETE | api/v1/sync/estate/regions/{uuid} | sync.estate.regions.destroy | M… |  |
| POST | api/v1/sync/estate/tariff_cards | sync.estate.tariff_cards.store | … |  |
| GET|HEAD | api/v1/sync/estate/tariff_cards/{uuid} | sync.estate.tariff_cards.s… |  |  |
| PUT | api/v1/sync/estate/tariff_cards/{uuid} | sync.estate.tariff_cards.u… |  |  |
| DELETE | api/v1/sync/estate/tariff_cards/{uuid} | sync.estate.tariff_cards.d… |  |  |
| POST | api/v1/sync/user/users | sync.user.users.store | Modules\CustomConf… |  |
| GET|HEAD | api/v1/sync/user/users/{uuid} | sync.user.users.show | Modules\Cust… |  |
| PUT | api/v1/sync/user/users/{uuid} | sync.user.users.update | Modules\Cu… |  |
| DELETE | api/v1/sync/user/users/{uuid} | sync.user.users.destroy | Modules\C… |  |
| POST | api/v1/telegram/auth | telegram.authsetAccount | Modules\CustomConf… |  |
| GET|HEAD | api/v1/telegram/auth/id/{telegram_id} | telegram.authcreateTelegram… |  |  |
| POST | api/v1/telegram/auth/{user_uuid} | telegram.authcreateAccount | Mod… |  |
| POST | api/v1/test/operation | test.operation | Modules\CustomConfig\Http\… |  |
| POST | api/v1/test/send-mails | test.send_mails | Modules\CustomConfig\Htt… |  |
| POST | api/v1/user/email/change | user.email.change | Modules\User\Http\Co… |  |
| GET|HEAD | api/v1/user/files/{file}/{conversion?} | user.files.show | Modules\… |  |
| GET|HEAD | api/v1/user/finance/account-purpose-list | user.finance.account_pur… |  |  |
| GET|HEAD | api/v1/user/finance/accounts | user.finance.accounts.index | Module… |  |
| GET|HEAD | api/v1/user/finance/active-currency-list | user.finance.active_curr… |  |  |
| GET|HEAD | api/v1/user/finance/active-real-currency-list | user.finance.active… |  |  |
| GET|HEAD | api/v1/user/finance/convert-amount | user.finance.convert_amount | … |  |
| GET|HEAD | api/v1/user/finance/currency-list | user.finance.currency_list | Mo… |  |
| GET|HEAD | api/v1/user/finance/document-type-list | user.finance.document_type… |  |  |
| GET|HEAD | api/v1/user/finance/documents | user.finance.documents.index | Modu… |  |
| GET|HEAD | api/v1/user/finance/documents/document-status-list | user.finance.d… |  |  |
| GET|HEAD | api/v1/user/finance/documents/export | user.finance.documents.expor… |  |  |
| POST | api/v1/user/finance/login | user.finance.login | Modules\Finance\Ht… |  |
| GET|HEAD | api/v1/user/finance/marketing-currency | user.finance.marketing_cur… |  |  |
| GET|HEAD | api/v1/user/finance/object-types | user.finance.object_types | Modu… |  |
| POST | api/v1/user/finance/operations/own-transfer | user.finance.operatio… |  |  |
| POST | api/v1/user/finance/operations/replenishment | user.finance.operati… |  |  |
| POST | api/v1/user/finance/operations/transfer-to-user | user.finance.oper… |  |  |
| POST | api/v1/user/finance/operations/withdrawal | user.finance.operations… |  |  |
| GET|HEAD | api/v1/user/finance/subject-types | user.finance.subject_types | Mo… |  |
| GET|HEAD | api/v1/user/finance/third-party-list | user.finance.third_party_lis… |  |  |
| GET|HEAD | api/v1/user/finance/transaction-type-list | user.finance.transactio… |  |  |
| GET|HEAD | api/v1/user/finance/transactions | user.finance.transactions.index |  |  |
| GET|HEAD | api/v1/user/finance/transactions/export | user.finance.transactions… |  |  |
| GET|HEAD | api/v1/user/finance/used-currency-list | user.finance.used_currency… |  |  |
| POST | api/v1/user/financial-password/change | user.financial_password.cha… |  |  |
| POST | api/v1/user/financial-password/recover | user.financial_password.re… |  |  |
| POST | api/v1/user/financial-password/reset | user.financial_password.rese… |  |  |
| GET|HEAD | api/v1/user/financial-password/reset-token/{token} | user.financial… |  |  |
| GET|HEAD | api/v1/user/marketing/active-volume-type-list | user.marketing.acti… |  |  |
| GET|HEAD | api/v1/user/marketing/activity-progress | user.marketing.activity_p… |  |  |
| GET|HEAD | api/v1/user/marketing/bonus-history | user.marketing.bonus_history |  |  |
| GET|HEAD | api/v1/user/marketing/bonus-history-graph | user.marketing.bonus_hi… |  |  |
| GET|HEAD | api/v1/user/marketing/bonus-history/export | user.marketing.bonus_h… |  |  |
| GET|HEAD | api/v1/user/marketing/last-invitations | user.marketing.last_invita… |  |  |
| GET|HEAD | api/v1/user/marketing/nodes/{node}/descendants | user.marketing.nod… |  |  |
| PATCH | api/v1/user/marketing/nodes/{node}/filling-settings | user.marketin… |  |  |
| GET|HEAD | api/v1/user/marketing/nodes/{node}/stats | user.marketing.nodes.sta… |  |  |
| GET|HEAD | api/v1/user/marketing/package-list | user.marketing.package_list | … |  |
| GET|HEAD | api/v1/user/marketing/package-stats-by-dates | user.marketing.packa… |  |  |
| GET|HEAD | api/v1/user/marketing/packages | user.marketing.packages.index | Mo… |  |
| POST | api/v1/user/marketing/packages/purchase | user.marketing.packages.p… |  |  |
| GET|HEAD | api/v1/user/marketing/packages/{package}/user-account-list | user.m… |  |  |
| GET|HEAD | api/v1/user/marketing/paid-bonus-stats-by-type | user.marketing.pai… |  |  |
| GET|HEAD | api/v1/user/marketing/partner-stats | user.marketing.partner_stats |  |  |
| GET|HEAD | api/v1/user/marketing/partner-stats-by-periods-comparison | user.ma… |  |  |
| GET|HEAD | api/v1/user/marketing/partner/{id}/rank-history | user.marketing.pa… |  |  |
| GET|HEAD | api/v1/user/marketing/partners/{partner} | user.marketing.partners |  |  |
| GET|HEAD | api/v1/user/marketing/partners/{partner}/rank-progress | user.marke… |  |  |
| GET|HEAD | api/v1/user/marketing/period-type-list | user.marketing.period_type… |  |  |
| GET|HEAD | api/v1/user/marketing/period-volumes/{period?} | user.marketing.per… |  |  |
| GET|HEAD | api/v1/user/marketing/periods | user.marketing.periods | Modules\Ma… |  |
| GET|HEAD | api/v1/user/marketing/profile | user.marketing.profile | Modules\Ma… |  |
| GET|HEAD | api/v1/user/marketing/rank-history | user.marketing.rank_history | … |  |
| GET|HEAD | api/v1/user/marketing/rank-list | user.marketing.rank_list | Module… |  |
| GET|HEAD | api/v1/user/marketing/rank-progress | user.marketing.rank_progress |  |  |
| GET|HEAD | api/v1/user/marketing/sponsor | user.marketing.sponsor | Modules\Ma… |  |
| GET|HEAD | api/v1/user/marketing/structure-package-buying | user.marketing.str… |  |  |
| GET|HEAD | api/v1/user/marketing/structure-package-buying/export | user.market… |  |  |
| GET|HEAD | api/v1/user/marketing/structure-package-history | user.marketing.st… |  |  |
| GET|HEAD | api/v1/user/marketing/structure-package-history-graph | user.market… |  |  |
| GET|HEAD | api/v1/user/marketing/structure-package-history/export | user.marke… |  |  |
| GET|HEAD | api/v1/user/marketing/structure-packages | user.marketing.structure… |  |  |
| GET|HEAD | api/v1/user/marketing/structure-packages/export | user.marketing.st… |  |  |
| GET|HEAD | api/v1/user/marketing/structure-rank-history | user.marketing.struc… |  |  |
| GET|HEAD | api/v1/user/marketing/structure-rank-history/export | user.marketin… |  |  |
| GET|HEAD | api/v1/user/marketing/structure-ranks | user.marketing.structure_ra… |  |  |
| GET|HEAD | api/v1/user/marketing/structure-ranks/export | user.marketing.struc… |  |  |
| GET|HEAD | api/v1/user/marketing/structure-stat | user.marketing.structure_sta… |  |  |
| GET|HEAD | api/v1/user/marketing/structures | user.marketing.structures.index |  |  |
| GET|HEAD | api/v1/user/marketing/top-leaders | user.marketing.top_leaders | Mo… |  |
| GET|HEAD | api/v1/user/marketing/volume-direction-list | user.marketing.volume… |  |  |
| GET|HEAD | api/v1/user/marketing/volume-event-list | user.marketing.volume_eve… |  |  |
| GET|HEAD | api/v1/user/marketing/volumes | user.marketing.volumes | Modules\Ma… |  |
| GET|HEAD | api/v1/user/marketing/volumes/export | user.marketing.volumes_expor… |  |  |
| GET|HEAD | api/v1/user/notification/events | user.notification.events.index | … |  |
| POST | api/v1/user/notification/events/read-all | user.notification.events… |  |  |
| POST | api/v1/user/notification/events/{event}/read | user.notification.ev… |  |  |
| GET|HEAD | api/v1/user/notification/fcm-token | user.notification.fcm_token.in… |  |  |
| POST | api/v1/user/notification/fcm-token | user.notification.fcm_token.st… |  |  |
| DELETE | api/v1/user/notification/fcm-token/{token} | user.notification.fcm*… |  |  |
| GET|HEAD | api/v1/user/notification/history | user.notification.history.index |  |  |
| GET|HEAD | api/v1/user/partner | user.partner | Modules\User\Http\Controllers\… |  |
| GET|HEAD | api/v1/user/partners/{id} | user.partners.show | Modules\User\Http\… |  |
| PUT | api/v1/user/partners/{id}/create-comment | user.partners.create_com… |  |  |
| GET|HEAD | api/v1/user/partners/{id}/descendants | user.partners.descendants |  |  |
| GET|HEAD | api/v1/user/partners/{id}/descendants/export | user.partners.descen… |  |  |
| GET|HEAD | api/v1/user/partners/{id}/descendants/fast | user.partners.descenda… |  |  |
| POST | api/v1/user/password/change | user.password.change | Modules\User\H… |  |
| POST | api/v1/user/phone/send-verification | user.phone.send_verification |  |  |
| GET|HEAD | api/v1/user/phone/verification | user.phone.show_verification | Mod… |  |
| POST | api/v1/user/phone/verify | user.phone.verify | Modules\User\Http\Co… |  |
| GET|HEAD | api/v1/user/profile | user.profile.show | Modules\CustomConfig\Http… |  |
| DELETE | api/v1/user/profile | user.profile.delete | Modules\User\Http\Contr… |  |
| POST | api/v1/user/profile | user.profile.update | Modules\CustomConfig\Ht… |  |
| GET|HEAD | api/v1/user/profile/agency-user-application | user.profile.showAgen… |  |  |
| POST | api/v1/user/profile/agency-user-application | user.profile.updateAg… |  |  |
| GET|HEAD | api/v1/user/profile/agency_role_list | user.profile.agencyRoleList |  |  |
| POST | api/v1/user/profile/agency_user_change | user.profile.agencyUserCha… |  |  |
| POST | api/v1/user/profile/image | user.profile.image | Modules\User\Http\… |  |
| DELETE | api/v1/user/profile/image | user.profile.image.delete | Modules\Use… |  |
| POST | api/v1/user/profile/lang-code | user.profile.set_language_code | Mo… |  |
| GET|HEAD | api/v1/user/profile/permissions | user.profile.permissions | Module… |  |
| GET|HEAD | api/v1/user/profile/telegram_assistant_url | user.profile.telegramA… |  |  |
| POST | api/v1/user/register | user.create | Modules\User\Http\Controllers\… |  |
| GET|HEAD | api/v1/user/roles | user.roles.index | Modules\User\Http\Controller… |  |
| GET|HEAD | api/v1/user/security | user.security.show | Modules\User\Http\Contr… |  |
| PUT | api/v1/user/security | user.security.update | Modules\User\Http\Con… |  |
| GET|HEAD | api/v1/user/security/event-list | user.security.event_list | Module… |  |
| POST | api/v1/user/security/send-code | user.security.send_code | Modules\… |  |
| GET|HEAD | api/v1/user/security/type-list | user.security.type_list | Modules\… |  |
| GET|HEAD | api/v1/user/security/{user}/settings | user.security.settings | Mod… |  |
| POST | api/v1/user/telegram/disable | user.telegram.disable | Modules\Tele… |  |
| POST | api/v1/user/telegram/generate-code | user.telegram.generate_code | … |  |
| GET|HEAD | api/v1/user/telegram/status | user.telegram.status | Modules\Telegr… |  |
| GET|HEAD | api/v1/user/verification | user.verification.show | Modules\Verific… |  |
| POST | api/v1/user/verification/send | user.verification.send | Modules\Ve… |  |
| GET|HEAD | api/v1/user/verification/stages | user.verification.stages.index | … |  |
| GET|POST|HEAD | broadcasting/auth | Illuminate\Broadcasting | BroadcastControll… |  |
| GET|HEAD | laravel-websockets | .. | ShowDashboard |  |
| GET|HEAD | laravel-websockets/api/{appId}/statistics | BeyondCode\LaravelWebSo… |  |  |
| POST | laravel-websockets/auth | BeyondCode\LaravelWebSockets | Authentica… |  |
| POST | laravel-websockets/event | BeyondCode\LaravelWebSockets | SendMessa… |  |
| POST | laravel-websockets/statistics | BeyondCode\LaravelWebSockets | WebS… |  |
| GET|HEAD | oauth/authorize | passport.authorizations.authorize | Laravel\Passp… |  |
| POST | oauth/authorize | passport.authorizations.approve | Laravel\Passpor… |  |
| DELETE | oauth/authorize | passport.authorizations.deny | Laravel\Passport … |  |
| GET|HEAD | oauth/clients | passport.clients.index | Laravel\Passport | ClientC… |
| POST | oauth/clients | passport.clients.store | Laravel\Passport | ClientC… |
| PUT | oauth/clients/{client_id} | passport.clients.update | Laravel\Passp… |  |
| DELETE | oauth/clients/{client_id} | passport.clients.destroy | Laravel\Pass… |  |
| GET|HEAD | oauth/personal-access-tokens | passport.personal.tokens.index | Lar… |  |
| POST | oauth/personal-access-tokens | passport.personal.tokens.store | Lar… |  |
| DELETE | oauth/personal-access-tokens/{token_id} | passport.personal.tokens.… |  |  |
| GET|HEAD | oauth/scopes | passport.scopes.index | Laravel\Passport | ScopeCont… |
| POST | oauth/token | passport.token | Laravel\Passport | AccessTokenContro… |
| POST | oauth/token/refresh | passport.token.refresh | Laravel\Passport | T… |
| GET|HEAD | oauth/tokens | passport.tokens.index | Laravel\Passport | Authorize… |
| DELETE | oauth/tokens/{token_id} | passport.tokens.destroy | Laravel\Passpor… |  |
| POST | telegram/webhook/{token} | telegram.webhook | Modules\Telegram\Http… |  |
|  |  |  |  |  |
| Showing | [1044] | routes |  |  |
